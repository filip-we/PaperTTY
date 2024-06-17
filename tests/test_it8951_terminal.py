import pytest

from papertty.papertty import PaperTTY, Settings

# Variables that you might have to tweak to get the test working in your environment and your screen model.
TRUE_TYPE_FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
VCOM = 1780

@pytest.fixture
def settings():
    settings = Settings(driver="IT8951", partial=True, encoding="latin_1")
    settings.args['vcom'] = VCOM
    settings.args['font'] = TRUE_TYPE_FONT
    settings.args['fontsize'] = 40
    return settings

def test_showtext(settings):
    ptty = settings.get_init_tty()

    ptty.set_tty_size("/dev/tty15", 20, 80)

    ptty.font = ptty.load_font(settings.args["font"], keep_if_not_found=True)
    ptty.showtext("Hello!\nWorld.", fill=ptty.black, portrait=True)

# TODO: print warning (somewhere) if no font has been defined. If it is not defined, no text will be printed.



