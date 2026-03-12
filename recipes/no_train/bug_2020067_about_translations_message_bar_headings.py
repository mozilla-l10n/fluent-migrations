# Any copyright is dedicated to the Public Domain.
# http://creativecommons.org/publicdomain/zero/1.0/

from fluent.migrate.helpers import transforms_from


def migrate(ctx):
    """Bug 2014459 - Migrate "New" badge for uplift, part {index}."""

    source = "browser/browser/browserContext.ftl"
    target = "browser/browser/tabbrowser.ftl"

    ctx.add_transforms(
        target,
        target,
        transforms_from(
            """
tab-note-panel-add-note-new-badge =
    .label = {COPY_PATTERN(from_path, "main-context-menu-new-feature-badge")}
""",
            from_path=source,
        ),
    )

