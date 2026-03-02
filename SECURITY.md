# Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do NOT open a public GitHub issue.**
2. Email: `security@example.com` (replace with your actual contact)
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact assessment

We will acknowledge receipt within 48 hours and provide a detailed response
within 5 business days.

## Threat Model

This project handles potentially sensitive government data. Key threat areas:

- **Data exfiltration**: All PII is redacted before processing.
- **Prompt injection**: Input sanitization is applied at the API boundary.
- **Dependency supply chain**: Dependencies are pinned and scanned via CodeQL.
- **Authentication bypass**: RBAC is enforced at the middleware layer.
