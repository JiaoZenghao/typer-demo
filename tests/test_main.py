try:
    from typer.testing import CliRunner
except ImportError:
    from click.testing import CliRunner  # Typer uses Click under the hood

from typer_demo.main import app
from typer_demo import __version__

runner = CliRunner()


def test_hello():
    result = runner.invoke(app, ["hello", "World"])
    assert result.exit_code == 0
    assert "Hello World" in result.stdout


def test_goodbye():
    result = runner.invoke(app, ["goodbye", "Alice"])
    assert result.exit_code == 0
    assert "Bye Alice!" in result.stdout


def test_goodbye_formal():
    result = runner.invoke(app, ["goodbye", "Bob", "--formal"])
    assert result.exit_code == 0
    assert "Goodbye, Ms./Mr. Bob. Have a good day." in result.stdout


def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert f"Typer Demo Version: {__version__}" in result.stdout


def test_help():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Show help information without command" in result.stdout
    assert "hello" in result.stdout
    assert "goodbye" in result.stdout
