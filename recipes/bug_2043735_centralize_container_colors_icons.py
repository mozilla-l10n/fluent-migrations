# Any copyright is dedicated to the Public Domain.
# http://creativecommons.org/publicdomain/zero/1.0/

from fluent.migrate import COPY_PATTERN
from fluent.migrate.helpers import transforms_from


def migrate(ctx):
    """Bug 2043735 - Centralize container colors and icons, part {index}."""

    source = "browser/browser/preferences/containers.ftl"
    target = "toolkit/toolkit/global/contextual-identity.ftl"

    ctx.add_transforms(
        target,
        target,
        transforms_from(
            """
user-context-color-blue =
    .label = {COPY_PATTERN(from_path, "containers-color-blue.label")}
user-context-color-green =
    .label = {COPY_PATTERN(from_path, "containers-color-green.label")}
user-context-color-yellow =
    .label = {COPY_PATTERN(from_path, "containers-color-yellow.label")}
user-context-color-orange =
    .label = {COPY_PATTERN(from_path, "containers-color-orange.label")}
user-context-color-red =
    .label = {COPY_PATTERN(from_path, "containers-color-red.label")}
user-context-color-pink =
    .label = {COPY_PATTERN(from_path, "containers-color-pink.label")}
user-context-color-purple =
    .label = {COPY_PATTERN(from_path, "containers-color-purple.label")}
user-context-color-toolbar =
    .label = {COPY_PATTERN(from_path, "containers-color-toolbar.label")}
user-context-icon-fingerprint =
    .label = {COPY_PATTERN(from_path, "containers-icon-fingerprint.label")}
user-context-icon-briefcase =
    .label = {COPY_PATTERN(from_path, "containers-icon-briefcase.label")}
user-context-icon-dollar =
    .label = {COPY_PATTERN(from_path, "containers-icon-dollar.label")}
user-context-icon-cart =
    .label = {COPY_PATTERN(from_path, "containers-icon-cart.label")}
user-context-icon-vacation =
    .label = {COPY_PATTERN(from_path, "containers-icon-vacation.label")}
user-context-icon-gift =
    .label = {COPY_PATTERN(from_path, "containers-icon-gift.label")}
user-context-icon-food =
    .label = {COPY_PATTERN(from_path, "containers-icon-food.label")}
user-context-icon-fruit =
    .label = {COPY_PATTERN(from_path, "containers-icon-fruit.label")}
user-context-icon-pet =
    .label = {COPY_PATTERN(from_path, "containers-icon-pet.label")}
user-context-icon-tree =
    .label = {COPY_PATTERN(from_path, "containers-icon-tree.label")}
user-context-icon-chill =
    .label = {COPY_PATTERN(from_path, "containers-icon-chill.label")}
user-context-icon-circle =
    .label = {COPY_PATTERN(from_path, "containers-icon-circle.label")}
user-context-icon-fence =
    .label = {COPY_PATTERN(from_path, "containers-icon-fence.label")}
""",
            from_path=source,
        ),
    )
