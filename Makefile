install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

build:
	uv build

package-install:

lint:
	uv run ruff check brain_games
