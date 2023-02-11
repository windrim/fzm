import sys

from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Input

from match import match


class Matches(Widget):

    search = reactive("")

    def render(self) -> str:
        return match(self.search)


class Prompt(App):

    def compose(self) -> ComposeResult:
        yield Input()
        yield Matches()

    def on_input_changed(self, event: Input.Changed) -> None:
        self.query_one(Matches).search = event.value

    def on_input_submitted(self, event: Input.Submitted) -> None:
        sys.exit(0)


if __name__ == "__main__":
    app = Prompt()
    app.run()
