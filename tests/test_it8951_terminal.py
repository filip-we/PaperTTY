import logging
import pytest
import time

from papertty.papertty import PaperTTY, Settings


log = logging.getLogger()
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

# Variables that you might have to tweak to get the test working in your environment and your screen model.
TRUE_TYPE_FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
VCOM = 1780

@pytest.fixture
def settings():
    settings = Settings(driver="IT8951", partial=True, encoding="latin_1")
    settings.args['vcom'] = VCOM
    settings.args['fontsize'] = 40
    return settings

@pytest.mark.parametrize(
    "font",
    [
        TRUE_TYPE_FONT,
        PaperTTY.defaultfont,
        None,
    ]
)
def test_showtext(settings, font):
    if font:
        settings.args['font'] = font
    log.info(f"Settings-args are: {settings.args}.")
    ptty = settings.get_init_tty()

    if font:
        ptty.font = ptty.load_font(settings.args["font"], keep_if_not_found=True)

    ptty.set_tty_size("/dev/tty15", 20, 80)
    ptty.showtext("Hello!\nWorld.", fill=ptty.black, portrait=True)

    log.info("Sleeping 1 second to allow you to see if the screen has any output.")
    time.sleep(1)


# TODO: print warning (somewhere) if no font has been defined. If it is not defined, no text will be printed.
#       When setting font to None, Papertty crashes. When ommitting it, nothing gets printed.


