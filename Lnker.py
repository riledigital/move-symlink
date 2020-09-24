import click
from tqdm import tqdm
from pathlib import Path
import shutil
import os
import yaml


@click.command()
@click.option("--config", default="config.yml", help="Set up your symlink paths here")
@click.option("--dry/--no-dry", default=True, help="Do a dry run to show path outcomes")
@click.option("--linkonly/--no-link", default=False, help="Only create symlinks from dest to src")
def run(config, dry, linkonly):
    if dry:
        click.secho(
            'No files will be moved or linked. --dry is enabled. Disable it with --no-dry. ',
            fg="blue")
    click.echo(f"Loaded {config}")
    cfg = load_yml(config)
    filemap = make_filemap(
        cfg['src'],
        to_path=cfg['dest']
    )

    if linkonly:
        click.secho(f"Only symlinking!")
        if not dry:
            operate(filemap, os.symlink, l_to_r=False)
    else:
        if not dry:
            operate(filemap, shutil.move, l_to_r=True)
            operate(filemap, os.symlink, l_to_r=False)
    pass


def load_yml(filein):
    with open(filein) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def make_filemap(infiles, to_path):
    ops = {}
    for file in infiles:
        f = Path(file)
        dest = to_path / Path(*(f.parts[4:]))
        ops[f] = dest
        # click.secho(f"rom...")
        click.secho(f"{f} -->", fg='blue')
        click.secho(f"{dest} \n", fg='green')
        # shutil.move(i, dest)
    return ops


def operate(filemap, func, l_to_r=True):
    click.secho(f'--dry="False" specified; operating {func}...', fg="red")
    for item in tqdm(filemap.items(), ncols=10):
        if l_to_r:
            click.secho(f"Running {func} from {item[0]}")
            func(item[0], item[1])
        else:
            click.secho(f"Running {func} from {item[1]}")
            func(item[1], item[0])
    click.secho(f'Finished performing {func}...', fg="green")


if __name__ == "__main__":
    run()
    pass
