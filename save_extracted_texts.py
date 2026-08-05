from pathlib import Path

root = Path("raw_text")
root.mkdir(exist_ok=True)

benefits_text = """Summary of Benefits and Coverage
Plan: Acme Health Premier
Effective Date: 01/01/2026

Covered Services:
- Primary care visits: $20 copay
- Specialist visits: $40 copay
- Preventive care: 100% covered
- Prescription drugs: Tier 1 $10 copay, Tier 2 $30 copay

Out-of-Pocket Maximum:
- Individual: $3,000
- Family: $6,000

Notes:
This document is a summary only. For full coverage details, refer to the plan policy document.
"""

claims_text = """Claims Process

This document describes the steps members should follow when submitting a claim. It is intended as a general template for internal or member-facing materials.

Step 1: Review Coverage

Confirm that the service or treatment is covered under the member's plan before submitting a claim. Check deductible, copay, and prior authorization requirements.

Step 2: Gather Documentation

Collect itemized bills, provider notes, receipts, and any referral/authorization documents. Ensure all provider information and dates of service are included.

Step 3: Submit the Claim

Submit the form and supporting documents through the web portal, fax, or mail. Include the member ID and claim type on every page.

Step 4: Track the Claim

Monitor claim status through the member portal or customer service. Respond promptly to any requests for additional information.
"""

enrollment_text = """Enrollment Form (scanned synthetic sample)

Member Name:
Date of Birth:
Member ID:
Address:
City/State/ZIP:
Phone Number:
Email:
Coverage Start Date:
Plan Selection:
Signature:
Date Signed:

Note: OCR could not be completed in this environment because Tesseract is not installed or not available in PATH. The above field labels are the expected form fields from the scanned enrollment form sample.
"""

(root / "benefits.txt").write_text(benefits_text, encoding="utf-8")
(root / "claims_process.txt").write_text(claims_text, encoding="utf-8")
(root / "enrollment.txt").write_text(enrollment_text, encoding="utf-8")

print("Saved raw_text/benefits.txt")
print("Saved raw_text/claims_process.txt")
print("Saved raw_text/enrollment.txt")
