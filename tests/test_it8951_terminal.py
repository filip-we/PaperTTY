from papertty.papertty import PaperTTY, Settings


def test_test():
    terminal_nr = 15
    settings = Settings(driver="IT8951", partial=True, encoding="latin_1")
    settings.args['vcom'] = 1780
    settings.args['font'] = "/".join(PaperTTY.defaultfont.split("/")[:-2]) + "/tom-thumb.pbm"
    settings.args['fontsize'] = 80
    ptty = settings.get_init_tty()

    ptty.set_tty_size(f"/dev/tty{terminal_nr}", 20, 80)

    max_dim = ptty.fit(portrait=True)

    ptty.font = ptty.load_font(settings.args["font"], keep_if_not_found=True)
    ptty.showtext("Hello!", fill=ptty.white, portrait=True)
    ptty.showtext("Hello!\nWorld.", fill=ptty.black, portrait=True)
    assert 1 == 2

# TODO: print warning (somewhere) if no font has been defined. If it is not defined, no text will be printed.



