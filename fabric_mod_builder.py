import argparse
import subprocess
import sys
from pathlib import Path

DEFAULT_VERSION = "1.21.5"
FABRIC_LOADER_VERSION = "0.15.10"
FABRIC_API_BASE = "0.100.0"

BUILD_GRADLE_TEMPLATE = """
plugins {{
    id 'fabric-loom' version '1.5-SNAPSHOT'
}}

repositories {{
    mavenCentral()
}}

dependencies {{
    minecraft "com.mojang:minecraft:{mc_version}"
    mappings "net.fabricmc:yarn:{mc_version}+build.1:v2"
    modImplementation "net.fabricmc:fabric-loader:{loader_version}"
    modImplementation "net.fabricmc.fabric-api:fabric-api:{api_version}+{mc_version}"
}}

loom {{
    splitEnvironmentSourceSets()
}}
"""

GRADLE_PROPERTIES = """org.gradle.jvmargs=-Xmx1G
"""

SETTINGS_GRADLE = "rootProject.name='{name}'\n"

def create_structure(base_dir: Path) -> None:
    (base_dir / 'src' / 'main' / 'java').mkdir(parents=True, exist_ok=True)
    (base_dir / 'src' / 'main' / 'resources').mkdir(parents=True, exist_ok=True)


def write_files(base_dir: Path, mc_version: str) -> None:
    build_gradle = BUILD_GRADLE_TEMPLATE.format(
        mc_version=mc_version,
        loader_version=FABRIC_LOADER_VERSION,
        api_version=FABRIC_API_BASE,
    )
    (base_dir / 'build.gradle').write_text(build_gradle)
    (base_dir / 'gradle.properties').write_text(GRADLE_PROPERTIES)
    (base_dir / 'settings.gradle').write_text(SETTINGS_GRADLE.format(name=base_dir.name))


def setup_gradle(base_dir: Path, run_client: bool) -> None:
    try:
        subprocess.check_call(['gradle', 'wrapper'], cwd=str(base_dir))
    except FileNotFoundError:
        print('Gradle is not installed. Please install Gradle and re-run this script.')
        return
    subprocess.call([str(base_dir / 'gradlew'), 'build'], cwd=str(base_dir))
    if run_client:
        subprocess.call([str(base_dir / 'gradlew'), 'runClient'], cwd=str(base_dir))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fabric mod project builder")
    parser.add_argument("name", help="Project directory")
    parser.add_argument(
        "--version",
        default=DEFAULT_VERSION,
        help="Target Minecraft version (default: %(default)s)",
    )
    parser.add_argument(
        "--run-client",
        action="store_true",
        help="Run gradle runClient after setup",
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Update an existing project to the given version",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target = Path(args.name)
    if not args.update:
        create_structure(target)
    write_files(target, args.version)
    setup_gradle(target, args.run_client)
    print(f"Fabric mod project ready at {target.resolve()}")


if __name__ == '__main__':
    main()
