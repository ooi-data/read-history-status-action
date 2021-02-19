# read-history-status-action

Github Actions To read status in yaml file.

## Inputs

### `file_path`

Path to yaml file relative to root.

## Outputs

### `status`

Status string found in file

## Example usage

```yaml
uses: ooi-data/read-history-status-action@main
with:
  file_path: .ci-helpers/file-status.yaml
```
