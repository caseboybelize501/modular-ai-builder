# Modular AI Builder

Modular AI Builder is a SMT-style AI engine where components share "commonality" across projects, recipes (configs) are composable, and the system scans for available "parts" (models) automatically.

## Features

- Feeder slots: where models live, numbered and indexed
- Feeder inventory scans: scans C: and D: for every GGUF, safetensor, ONNX, etc.
- Siemens Desk software: web UI showing all slots, recipes, commonality
- Recipes: YAML files defining what roles a build needs
- Commonality capture: keeps shared models loaded, counts saves
- Base → variant divergence: project recipes inherit base, override only what changes
- Process multiplier: calculated as N/swap ratio
- Multi-head placement: runs multiple recipes concurrently sharing loaded slots

## Getting Started

1. Clone the repository:
   bash
   git clone https://github.com/yourusername/modular-ai-builder.git
   cd modular-ai-builder
   
2. Install dependencies:
   bash
   pip install -r requirements.txt
   
3. Run the application:
   bash
   python setup_manager/app.py
   

## Usage

- Access the Siemens Desk software at `http://localhost:5000`.
- Configure recipes in the `recipes/` directory.
- Manage feeder slots and inventory scans in the `feeder_slots/` directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
