#!/usr/bin/env python3
"""Ontario Retail Store Permit Checklist Generator - by Dust 2 Engineering Inc., Mississauga, Ontario.
Preliminary information only. Not engineering advice and not a code review.
Verify every item with your designer and the local building department.
"""
import argparse, pathlib
CONFIG = {'title': 'Ontario Retail Store Permit Checklist Generator', 'tagline': 'Ontario Retail Store Permit Checklist Generator by Dust 2 Engineering Inc.', 'unit_label': 'Staff + typical customers (occupant guide)', 'flags': [{'arg': 'facade-changes', 'label': 'Storefront / facade changes'}, {'arg': 'mezzanine-or-racking', 'label': 'Mezzanine or high storage racking'}, {'arg': 'change-of-use', 'label': 'The unit was not retail before (change of use)'}], 'sections': [{'title': '1. Application basics (always required)', 'items': ['Municipal building permit application form, completed and signed by the owner or authorized agent', 'Schedule 1: Designer Information form for each qualified designer on the project', 'Owner authorization if the applicant is not the property owner, plus the lease for a tenant fit-out if the city asks for it', 'Zoning review first: confirm the retail use, floor area and any outdoor elements are permitted at this address', 'Occupant load calculation shown on the floor plan, based on the actual layout']}, {'title': '2. Architectural drawings', 'items': ['Floor plan: sales area, stockroom, office, fitting rooms and washrooms clearly labelled', 'Barrier-free entrance, path of travel and barrier-free washroom where required', 'Demising walls and fire separations between your unit and neighbours shown with ratings', 'Exit signs, emergency lighting, travel distances and the number of exits for the sales floor', 'Storage height and stockroom layout shown - high storage can change sprinkler requirements']}, {'title': 'Storefront and facade', 'when': 'facade-changes', 'items': ['Storefront drawings: new glazing, doors and any structural lintel changes', 'Sign band and sign permit drawings - the sign permit is a separate application', 'Landlord and plaza approvals for exterior changes, plus city facade rules in some downtown areas']}, {'title': 'Mezzanine and high racking', 'when': 'mezzanine-or-racking', 'items': ['Structural drawings for the mezzanine or racking, stamped by an Ontario P.Eng.', 'Confirm sprinklers and fire alarm coverage for the storage height and commodity being stored - do not assume the existing system is enough']}, {'title': 'Change of use', 'when': 'change-of-use', 'items': ['Change of use review: the existing unit must be checked against current code for retail use, even if construction is minor', 'Washroom count, barrier-free and exit requirements are re-checked for the new use']}, {'title': '3. Mechanical, plumbing and electrical', 'items': ['HVAC drawings for the sales floor, stockroom and washrooms, including any rooftop unit changes', 'Plumbing drawings for washrooms and any added sinks, with backflow preventer where required', 'Electrical drawings: panel, sales-floor lighting, receptacles, exit signs and emergency lighting circuits', 'Fire alarm verification if the building system is affected by the new layout; sprinkler requirements to be confirmed with the building department']}, {'title': '4. Other approvals (not part of the building permit)', 'items': ['Sign permit (separate), business licence from the city after the permit closes', 'Check the lease and plaza rules for storefront, signage and construction hours before submitting']}, {'title': 'Before you submit', 'items': ['One combined PDF set: architectural, mechanical, plumbing, electrical and structural (if any), all consistent with each other', 'All drawing sets use the same address, unit number, floor area and counts', 'Designs that require an engineer must be stamped by a licensed Ontario P.Eng.; BCIN designer information where applicable', 'Book a pre-consultation or zoning check with the city if the use or layout is not clearly permitted']}]}
def main():
    p = argparse.ArgumentParser(description=CONFIG["tagline"])
    p.add_argument("--city", default="Toronto")
    p.add_argument("--area-sqft", type=int, default=1200)
    p.add_argument("--units", type=int, default=0, help=CONFIG["unit_label"])
    for f in CONFIG["flags"]:
        p.add_argument("--" + f["arg"], action="store_true", help=f["label"])
    p.add_argument("--output", default="")
    a = p.parse_args()
    L = []
    L.append("# " + CONFIG["title"] + " - Ontario")
    L.append("")
    L.append("**City:** %s | **Area:** %d sq ft | **%s:** %d" % (a.city, a.area_sqft, CONFIG["unit_label"], a.units))
    L.append("")
    L.append("> Preliminary checklist generated with the free open-source " + CONFIG["title"] + " by Dust 2 Engineering Inc., Mississauga, Ontario. Verify every item with your designer and the local building department before submitting.")
    L.append("")
    for s in CONFIG["sections"]:
        if s.get("when") and not getattr(a, s["when"].replace("-", "_")):
            continue
        L.append("## " + s["title"])
        for it in s["items"]:
            L.append("- [ ] " + it)
        L.append("")
    L.append("---")
    L.append("Generated by the " + CONFIG["title"] + ", a free open-source tool by Dust 2 Engineering Inc. Dust 2 Engineering Inc. provides building permit drawings (architecture, HVAC, plumbing, sprinkler and electrical) stamped by an Ontario P.Eng. in the Greater Toronto Area, including Toronto, Mississauga, Brampton, Vaughan, Markham and Hamilton, for a flat fee of $3,500 to $5,000. This checklist is preliminary information only and is not engineering advice.")
    L.append("")
    out = "\n".join(L)
    if a.output:
        pathlib.Path(a.output).write_text(out, encoding="utf-8")
        print("Wrote " + a.output)
    else:
        print(out)
if __name__ == "__main__":
    main()
