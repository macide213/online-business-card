# DB Digital Business Card

A professional, mobile-first digital business card with integrated vCard management and instant-scan QR code functionality.

## 🚀 Features

- **Professional Redesign:** Modern, clean "Corporate-Professional" UI built with Vanilla CSS (OKLCH colors).
- **Interactive Buttons:** Quick-action grid for Calling, WhatsApp, Emailing, and Saving Contacts.
- **Smart vCard:** Cross-platform compatible (vCard 3.0) with primary number prioritization.
- **Offline QR Code:** High-density QR code that embeds your full contact info for immediate scanning without an internet connection.
- **Automation Script:** Simple Python utility to update your details and regenerate assets.

## 🛠 Management

The repository includes a utility script `update_vcard.py` to manage your contact details.

### How to update your information

1. **Prepare the environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install qrcode[pil] vobject
   ```

2. **Run the update script:**
   ```bash
   python update_vcard.py --first "Derek" --last "Bartoli" --emails "email@example.com" --phones "+14075698409" "+14077445181" --primary_phone 0
   ```

3. **Options:**
   - `--first`: First Name
   - `--last`: Last Name
   - `--emails`: List of email addresses
   - `--phones`: List of phone numbers
   - `--primary_phone`: Index (0-based) of the number to set as Primary/Preferred.
   - `--note`: A brief bio or note for the contact.

The script will automatically update `vcard.vcf` and regenerate `qrcode.png`.

## 🎨 Branding

This project uses the official DB Branding Kit assets located in `assets/branding/`.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
