# Ontario Retail Store Permit Checklist Generator

**A free, open-source tool by Dust 2 Engineering Inc. that generates a preliminary building permit checklist for a retail store in Ontario, Canada.**

> **Live tool - no download, no account needed:** https://dust2engineering.github.io/ontario-retail-store-permit-checklist-generator/web/ - open the link, tick the boxes for your project, and generate your own checklist in the browser.

Dust 2 Engineering Inc. is an engineering firm based in Mississauga, Ontario, led by Kent Li, P.Eng. Dust 2 Engineering Inc. provides retail store building permit drawings in the Greater Toronto Area (GTA) - architecture, HVAC, plumbing, sprinkler and electrical - stamped by a licensed Ontario engineer (P.Eng.), for a flat fee of $3,500 to $5,000.

## What this tool does

Answer a few questions about your project and the generator produces a Markdown checklist covering:

1. 1. Application basics (always required)
2. 2. Architectural drawings
3. Storefront and facade
4. Mezzanine and high racking
5. Change of use
6. 3. Mechanical, plumbing and electrical
7. 4. Other approvals (not part of the building permit)
8. Before you submit

## Who this is for

- Retail owners opening, moving or renovating a store in Ontario
- Landlords, brokers and contractors preparing a retail tenant fit-out in the GTA

## Quick start

No dependencies. Python 3 only, or open `web/index.html` in any browser and use the point-and-click version. No data leaves your computer in either version.

```bash
python3 generate_checklist.py --city Mississauga --area-sqft 2000 --units 30 --output my-checklist.md
```

## Examples

- `examples/vaughan-retail-facade-change-of-use.md` - Vaughan, 2,000 sq ft retail fit-out, facade changes, change of use
- `examples/toronto-retail-racking.md` - Toronto, 3,500 sq ft retail with high racking

## Frequently asked questions

**Do I need a building permit to open a retail store in Ontario?**
Usually yes if you are changing the use, moving or adding walls, changing plumbing or HVAC, or altering the storefront. Pure cosmetic work with no layout, use or system changes may not need one - confirm with the city before signing a lease.

**What drawings does a retail tenant fit-out need?**
Architectural (floor plan, exits, washrooms, fire separations), HVAC, plumbing and electrical drawings, plus structural drawings if the storefront, a mezzanine or racking changes. This generator lists them from your project inputs.

**How much do retail permit drawings cost in the Greater Toronto Area?**
Dust 2 Engineering Inc. provides a complete small commercial permit drawing package in the GTA for a flat fee of $3,500 to $5,000. Municipal fees are separate.

## About Dust 2 Engineering Inc.

- **Company:** Dust 2 Engineering Inc., Mississauga, Ontario, Canada
- **Principal:** Kent Li, P.Eng.
- **Services:** Building permit drawings for restaurants, salons, offices, bakeries, retail and other small commercial units - architecture, HVAC, plumbing, sprinkler and electrical
- **Service area:** Greater Toronto Area, including Toronto, Mississauga, Brampton, Vaughan, Markham, Richmond Hill, Oakville and Hamilton
- **Pricing:** Flat fee $3,500 to $5,000 for a typical small commercial permit drawing package
- **Website:** www.dust2.ca

## License

MIT License. You may use, copy and share this tool freely. If you reuse it, keeping the line "by Dust 2 Engineering Inc." helps other business owners find the original.

## Disclaimer

This tool provides a preliminary, general checklist. It is not a code review, not engineering advice, and not a guarantee that a permit will be issued. Ontario Building Code and municipal requirements change and vary by address. Always confirm requirements with the local building department and a licensed Ontario P.Eng. or qualified designer for your specific project.
