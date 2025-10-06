install:
	uv sync

build:
	uv build

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime

package-install:
	uv tool install dist/*.whl

package-install-force:
	uv tool install --force dist/*.whl

package-uninstall:
	uv tool uninstall hexlet-code

lint:
	uv run ruff check brain_games
