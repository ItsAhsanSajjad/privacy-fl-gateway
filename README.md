# privacy-fl-gateway

![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python&logoColor=white)
![Flower](https://img.shields.io/badge/Flower-1.9-FF6F00?logo=data:image/svg+xml;base64,)
![License](https://img.shields.io/badge/license-MIT-green)
![CI](https://github.com/USERNAME/privacy-fl-gateway/actions/workflows/ci.yml/badge.svg)

**Federated learning aggregation gateway with differential privacy for
cross-departmental model training without moving raw data.**

## Architecture

```mermaid
flowchart TB
    subgraph Department A
        CA[FL Client A]
    end
    subgraph Department B
        CB[FL Client B]
    end
    subgraph Gateway
        S[FL Server] --> AGG[FedAvg Aggregator]
        AGG --> DP[DP Noise Injector]
        DP --> MW[Model Weights Store]
    end
    CA -- gRPC/TLS --> S
    CB -- gRPC/TLS --> S
```

## Quick Start

```bash
pip install -e ".[dev]"
pytest -v
python -m src.server
```

## Docker

```bash
docker compose up --build
```

## Threat Model

| Threat | Mitigation |
|---|---|
| Model inversion attacks | Differential privacy noise injection (ε-bounded) |
| Gradient leakage | Secure aggregation protocol |
| Unauthorized node joining | JWT-based client authentication |
| Man-in-the-middle | Mandatory TLS for all gRPC channels |

## Project Structure

```
src/
├── server.py       # FL aggregation server
├── client.py       # FL client template
├── strategy/
│   └── dp.py       # Differential privacy strategy
└── auth/
    └── jwt.py      # JWT validation for nodes
tests/              # Unit tests
docs/adr/           # Architecture Decision Records
```

## License

MIT — see [LICENSE](LICENSE).
