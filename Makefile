install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:

lint:
	uv run ruff check brain_games

