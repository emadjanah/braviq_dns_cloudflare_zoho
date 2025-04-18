![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/emadjanah/braviq_dns_cloudflare_zoho/cloudflare_dns.yml?branch=main)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Made with GitHub Actions](https://img.shields.io/badge/Made%20with-GitHub%20Actions-blue?logo=github-actions)
# braviq_dns_cloudflare_zoho

**Automated DNS Setup for Cloudflare + Zoho Mail EU Integration**

This repository was developed by **Emad Janah**, founder of **BRAVIQ GROUP**, to enable automatic DNS configuration for the domain `braviq.group` using GitHub Actions, Cloudflare API, and Zoho Mail EU servers.

---

## Features

- Automatically updates MX, SPF, DKIM, and DMARC records for Zoho Mail EU.
- Uses GitHub Actions with secure API token handling.
- Supports zip-based script deployment via GitHub workflow.

---

## Usage Instructions

### 1. Prepare the Repository

- Clone this repo or upload your DNS script as a `.zip` file:
  - `braviq_dns_cloudflare_zoho.zip`
- Ensure that the `cloudflare_dns.yml` GitHub Actions workflow is in:
  - `.github/workflows/cloudflare_dns.yml`

---

### 2. Set Cloudflare API Token

Go to:
``Settings > Secrets and Variables > Actions > New repository secret``

- Name: `CLOUDFLARE_API_TOKEN`
- Value: Your Cloudflare token with DNS Edit permissions

---

### 3. Run the Workflow

- Go to the **Actions** tab
- Select `Cloudflare DNS Update`
- Click on **Run workflow**

---

## Folder Structure

```bash
.github/
  workflows/
    cloudflare_dns.yml
scripts/
  cloudflare_dns_updater_enhanced.py
braviq_dns_cloudflare_zoho.zip
BENİOKU.md
## License

MIT License – Feel free to fork, enhance, or contribute.
## License

MIT License – Feel free to fork, enhance, or contribute.

---

## Türkçe Açıklama

Bu repozituvar, **Emad Janah** tarafından geliştirilmiştir ve braviq.group alan adı için Zoho Mail EU ile entegre şekilde otomatik Cloudflare DNS yapılandırmasını sağlar.

### Özellikler
- MX, SPF, DKIM ve DMARC kayıtlarını otomatik olarak günceller.
- Güvenli GitHub Actions + API Token kullanımı.
- Zip tabanlı script çalıştırma desteği.

### Nasıl Kullanılır?
1. `Secrets` bölümüne `CLOUDFLARE_API_TOKEN` değerinizi ekleyin.
2. `Actions > Cloudflare DNS Update > Run workflow` adımlarını takip edin.

---

Herhangi bir katkı, öneri veya fork'a açıktır.
