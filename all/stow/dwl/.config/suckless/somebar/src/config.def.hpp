// somebar - dwl bar
// See LICENSE file for copyright and license details.

#pragma once
#include "common.hpp"

constexpr bool topbar = true;

constexpr int paddingX = 6;
constexpr int paddingY = 5;

// See https://docs.gtk.org/Pango/type_func.FontDescription.from_string.html
constexpr const char* font = "Cascadia Code 10";

constexpr ColorScheme colorInactive = {Color(0x6a, 0x6f, 0x87), Color(0x1a, 0x1b, 0x26)};
constexpr ColorScheme colorActive = {Color(0xc0, 0xca, 0xf5), Color(0x1a, 0x1b, 0x26)};
constexpr const char* termcmd[] = {"foot", nullptr};

static std::vector<std::string> tagNames = {
	"Z", "X", "C",
	"V", "A", "S",
	"D", "F",
};

constexpr Button buttons[] = {
	{ ClkStatusText,   BTN_RIGHT,  spawn,      {.v = termcmd} },
};
