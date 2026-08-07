# Any copyright is dedicated to the Public Domain.
# http://creativecommons.org/publicdomain/zero/1.0/

from fluent.migrate.helpers import transforms_from


def migrate(ctx):
    """Bug 2052034 - Reuse theme-picker theme names for about:addons theme names, part {index}."""

    source = "toolkit/toolkit/global/theme-picker.ftl"
    target = "browser/browser/appExtensionFields.ftl"
    target_about_addons = "toolkit/toolkit/about/aboutAddons.ftl"

    ctx.add_transforms(
        target,
        target,
        transforms_from(
            """
extension-default-theme-name2 = {COPY_PATTERN(from_path, "theme-picker-default.label")}
extension-nova-sun-name = {COPY_PATTERN(from_path, "theme-picker-sun.label")}
extension-nova-spark-name = {COPY_PATTERN(from_path, "theme-picker-spark.label")}
extension-nova-flame-name = {COPY_PATTERN(from_path, "theme-picker-flame.label")}
extension-nova-flare-name = {COPY_PATTERN(from_path, "theme-picker-flare.label")}
extension-nova-lavender-name = {COPY_PATTERN(from_path, "theme-picker-lavender.label")}
extension-nova-dusk-name = {COPY_PATTERN(from_path, "theme-picker-dusk.label")}
extension-nova-lagoon-name = {COPY_PATTERN(from_path, "theme-picker-lagoon.label")}
extension-nova-pine-name = {COPY_PATTERN(from_path, "theme-picker-pine.label")}
extension-nova-tide-name = {COPY_PATTERN(from_path, "theme-picker-tide.label")}
extension-nova-ash-name = {COPY_PATTERN(from_path, "theme-picker-ash.label")}
extension-nova-smoke-name = {COPY_PATTERN(from_path, "theme-picker-smoke.label")}
""",
            from_path=source,
        ),
    )

    ctx.add_transforms(
        target_about_addons,
        target_about_addons,
        transforms_from(
            """
themes-mode-light =
    .label = {COPY_PATTERN(from_path, "theme-picker-mode-light")}
themes-mode-dark =
    .label = {COPY_PATTERN(from_path, "theme-picker-mode-dark")}
themes-mode-device =
    .label = {COPY_PATTERN(from_path, "theme-picker-mode-device")}
aboutaddons-linux-theme-colors-checkbox-label =
    .label = {COPY_PATTERN(from_path, "theme-picker-use-linux-theme.label")}
""",
            from_path=source,
        ),
    )
