import sys
import re
import click
import tempfile

from getoc.mirror import Mirror

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.argument("version")
def dl(version):
    """Download an OpenShift Client"""
    # If user only enters X.Y (e.g. 4.1, 4.6) then let's prepend "latest" to it...
    major_minor = re.compile(r"^\d\.\d$")
    if major_minor.match(version):
        version = "latest-%s" % version

    # Find the version to download
    mirror = Mirror()
    click.secho("Checking download mirror for %s..." % version, fg="yellow")
    if not mirror.is_version_published(version):
        click.secho("Version %s unavailable" % version, sys.stderr, fg="red")
    else:
        click.secho("Found %s!" % version, fg="green")

    # Download it
    with tempfile.NamedTemporaryFile() as newfile:
        click.secho("Downloading %s" % version, fg="green")
        mirror.download(version, newfile)

        # TODO: Move into store