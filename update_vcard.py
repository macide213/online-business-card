import vobject
import qrcode
import os
import argparse

def update_vcard(first_name, last_name, emails, phones, primary_phone_index, socials, note, photo_path=None):
    vcard = vobject.vCard()
    
    # Name
    vcard.add('n')
    vcard.n.value = vobject.vcard.Name(family=last_name, given=first_name)
    vcard.add('fn')
    vcard.fn.value = f"{first_name} {last_name}"
    
    # Emails
    for i, email in enumerate(emails):
        e = vcard.add('email')
        e.value = email
        e.type_param = 'INTERNET'
        if i == 0:
            e.type_param = ['INTERNET', 'PREF']

    # Phones
    for i, phone in enumerate(phones):
        p = vcard.add('tel')
        p.value = phone
        if i == primary_phone_index:
            p.type_param = ['CELL', 'PREF']
        else:
            p.type_param = ['CELL']

    # Note
    if note:
        vcard.add('note')
        vcard.note.value = note

    # Socials (X-SOCIALPROFILE)
    for platform, url in socials.items():
        s = vcard.add('x-socialprofile')
        s.type_param = platform
        s.value = url

    # Save VCF
    vcf_content = vcard.serialize()
    with open('vcard.vcf', 'w') as f:
        f.write(vcf_content)
    print("vcard.vcf updated.")

    # Generate QR Code (Full vCard Data for "Create Contact")
    qr = qrcode.QRCode(
        version=None,  # Auto-select version based on data size
        error_correction=qrcode.constants.ERROR_CORRECT_M, # Better balance for scanability
        box_size=10,
        border=4,
    )
    qr.add_data(vcf_content)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    print("qrcode.png updated (embedded vCard).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update vCard and QR Code')
    parser.add_argument('--first', default='Derek', help='First Name')
    parser.add_argument('--last', default='Bartoli', help='Last Name')
    parser.add_argument('--emails', nargs='+', default=['derek@bartoli.me'], help='Email addresses')
    parser.add_argument('--phones', nargs='+', default=['+14077445181'], help='Phone numbers')
    parser.add_argument('--primary_phone', type=int, default=0, help='Index of primary phone (0-based)')
    parser.add_argument('--note', default='Freelance Developer', help='Note/Bio')
    
    args = parser.parse_args()
    
    # Example Socials
    social_profiles = {
        'LinkedIn': 'https://www.linkedin.com/in/derek-bartoli',
        'GitHub': 'https://github.com/macide213',
        'Twitter': 'https://x.com/DerekBartoli'
    }
    
    update_vcard(args.first, args.last, args.emails, args.phones, args.primary_phone, social_profiles, args.note)
