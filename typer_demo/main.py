import typer
from typer_demo import __version__

app = typer.Typer()


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye, Ms./Mr. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


def version_callback(value: bool):
    if value:
        typer.echo(f"Typer Demo Version: {__version__}")
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show the application's version and exit.",
    ),
    ctx: typer.Context = typer.Context,
):
    """
    Show help information without command
    """
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()


if __name__ == "__main__":
    app()
