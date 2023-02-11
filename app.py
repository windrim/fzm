from textual.app import App, ComposeResult, events
from textual.containers import Container
from textual.widgets import TextLog


class FZM(App):

    BINDINGS = [("m", "multi_select", "Select multiple matches")]

    def compose(self) -> ComposeResult:
        yield TextLog()

    def on_key(self, event: events.Key) -> None:
        self.query_one(TextLog).write(event)


if __name__ == "__main__":
    app = FZM()
    app.run()
