# Catalog Schema

`catalog.json` uses schema version 2.

## Feature flags

Capability fields use tri-state JSON values:

- `true`: support was verified.
- `false`: unsupported or not applicable was verified.
- `null`: not verified during the current review; do not treat as false.

## Required entry fields

- `name`
- `slug`
- `category`
- `provider`
- `installer`
- `installer_type`
- `binary`
- `url`
- `open_source`
- `local_models`
- `openai_compatible`
- `mcp`
- `acp`
- `subscription_auth`
- `api_key`
- `daemon_server`
- `last_verified`
- `official_source`

## Design rules

1. Prefer upstream project documentation, upstream repositories, or the project's official package-registry page.
2. Keep installer commands shell-copyable and non-interactive where the upstream supports that.
3. Do not infer unsupported capabilities. Use `null`.
4. Update `last_verified` whenever installer or capability data is rechecked.
5. Preserve unique `slug` values so downstream launchers can use them as stable identifiers.
