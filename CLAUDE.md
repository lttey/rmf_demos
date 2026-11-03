# rmf_demos

Open-RMF demo worlds (hotel, office, clinic, …), CHART's working copy.

## Stack
ROS 2 Jazzy, Gazebo (`rmf_demos_gz`), Python fleet adapters (EasyFullControl).

## Structure
- `rmf_demos/launch/`: per-world launch files and `common.launch.xml`, which starts the shared RMF core nodes
- `rmf_demos_gz/launch/`: simulation wrappers, e.g. `hotel.launch.xml`
- `rmf_demos_fleet_adapter/`: EasyFullControl demo adapter, plus `manage_lane.py` for lane open/close
- `rmf_demos_maps/`: building maps and nav graphs

## Useful launch args (`common.launch.xml`)
- `use_lift_manager` (default `false`): run `rmf_lift_manager` instead of `lift_supervisor`. Only one of them runs at a time.
- `lift_manager_config`: params file for the lift manager (default: its installed `config/lift_manager.yaml`)
- `use_reservation_node`, `use_site_map`, `headless`, `server_uri`

## Conventions
Follow upstream Open-RMF style here. CHART naming rules apply to new CHART-owned files.

## Don't touch
- Upstream map assets in `rmf_demos_maps`, unless the change is deliberate

## Recent changes
- 2026-10-20 (`lift_sharing`): added `use_lift_manager` / `lift_manager_config` to `common.launch.xml`. Before this, `lift_supervisor` and `lift_manager` both ran at once.
