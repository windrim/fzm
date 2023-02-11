import sys

from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import DataTable, Input

from fzm.match import match


class Matches(DataTable):

    search = reactive("")

    def watch_search(self, search) -> None:
        self.clear()
        self.add_rows(match(search))


class Prompt(App):

    def compose(self) -> ComposeResult:
        yield Input()
        yield Matches()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("name", "score", "idx")

    def on_input_changed(self, event: Input.Changed) -> None:
        self.query_one(Matches).search = event.value

    def on_input_submitted(self, event: Input.Submitted) -> None:
        sys.exit(0)


def main():
    app = Prompt()
    app.run()
