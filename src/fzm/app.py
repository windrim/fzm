import sys

from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import DataTable, Input

from fzm.match import match


class Matches(DataTable):

    def __init__(
        self, 
        source: list[str],
        *, 
        show_header: bool = True, 
        fixed_rows: int = 0, 
        fixed_columns: int = 0, 
        zebra_stripes: bool = False, 
        header_height: int = 1, 
        show_cursor: bool = True, 
        name: str | None = None, 
        id: str | None = None, 
        classes: str | None = None
        ) -> None:
        self.source = source
        super().__init__(
            show_header=show_header, fixed_rows=fixed_rows, 
            fixed_columns=fixed_columns, zebra_stripes=zebra_stripes, 
            header_height=header_height, show_cursor=show_cursor, 
            name=name, id=id, classes=classes
        )

    search = reactive("")

    def watch_search(self, search) -> None:
        self.clear()
        self.add_rows(match(search, self.source))


class Prompt(App):

    def __init__(
        self, 
        # data parameter required on startup
        source: list[str],
        # these two below args have type hints I couldn't import ...
        driver_class = None, 
        css_path = None, 
        watch_css: bool = False
        ):
        self.source = source
        super().__init__(driver_class, css_path, watch_css)

    def compose(self) -> ComposeResult:
        yield Input()
        # passing data parameter to table
        yield Matches(source=self.source)

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("name", "score", "idx")

    def on_input_changed(self, event: Input.Changed) -> None:
        self.query_one(Matches).search = event.value

    def on_input_submitted(self, event: Input.Submitted) -> None:
        sys.exit(0)


def run(source: list[str]):
    app = Prompt(source=source)
    app.run()
    
