# Any copyright is dedicated to the Public Domain.
# http://creativecommons.org/publicdomain/zero/1.0/

import re
from fluent.migrate.transforms import TransformPattern, COPY_PATTERN
from fluent.migrate.helpers import transforms_from
import fluent.syntax.ast as FTL


class STRIP_ELLIPSIS(TransformPattern):
    def visit_TextElement(self, node):
        node.value = re.sub(r"(?:…|\.\.\.)$", "", node.value)
        return node


def migrate(ctx):
    """Bug 1971841 - Convert Sync section to config-based prefs, part {index}"""
    path = "browser/browser/preferences/preferences.ftl"

    ctx.add_transforms(
        path,
        path,
        transforms_from(
            """
sync-device-name-input =
    .aria-label = { COPY_PATTERN(path1, "sync-device-name-header") }
    .placeholder = { $placeholder }
""",
            path1=path,
        ),
    )

    ctx.add_transforms(
        path,
        path,
        [
            FTL.Message(
                id=FTL.Identifier("sync-device-name-change-2"),
                attributes=[
                    FTL.Attribute(
                        id=FTL.Identifier("label"),
                        value=STRIP_ELLIPSIS(path, "sync-device-name-change.label"),
                    ),
                    FTL.Attribute(
                        id=FTL.Identifier("accesskey"),
                        value=COPY_PATTERN(path, "sync-device-name-change.accesskey"),
                    ),
                ],
            ),
        ],
    )
