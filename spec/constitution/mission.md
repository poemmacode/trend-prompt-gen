# Mission — TrendPrompt Engine

## What We Build

TrendPrompt Engine is a dual-engine software tool:

1. **Trend-Hunter:** Real-time trend search and analysis engine for a given market niche. It aggregates data from:
   - Google Trends (rising terms, Related queries, Interest by region)
   - Amazon Best Sellers and Movers & Shakers
   - Etsy Trending and popular searches
   - Social media: Twitter/X trending topics, TikTok hashtag virality, Pinterest trending pins

2. **Prompt-Writer:** Image AI prompt generation engine (Midjourney, DALL-E, Stable Diffusion) based on discovered trends. Generates 8-10 prompts per trend in a standardized format.

## Who It's For

- **Digital content creators** looking for fresh ideas backed by real data.
- **Print-on-demand sellers** (Redbubble, Merch by Amazon, TeeSpring) who need up-to-date design trends.
- **Graphic designers** wanting inspiration based on what's actually selling.
- **Social media managers** seeking trending visual content for their clients.
- **E-commerce entrepreneurs** who want to validate niches before creating products.

## Key System Objectives

1. **Full automation:** The user enters a niche and receives a complete report with no manual intervention.
2. **Verifiable data:** Every reported trend includes the exact source (URL or reference) so the user can validate it.
3. **Ready-to-use prompts:** Generated prompts can be copied with one click and work directly in AI tools.
4. **Speed:** A complete report should be generated in under 60 seconds (target).
5. **Niche accuracy:** Results must be relevant to the specific niche, not generic.

## Expected Output Format

Each trend in the report must contain:

```markdown
## [Trend Title]

**Suggested product:** [Product description based on the trend]

```prompt
[The complete prompt for generative image AI, ready to copy]
```

**Sources:**
- [URL or reference 1]
- [URL or reference 2]
```

## Success Metrics

- Trend relevance rate per niche ≥ 85% (manual validation on sample).
- Average report generation time < 60 seconds.
- Generated prompts producing useful results on first iteration ≥ 70%.
- Zero scraping errors on primary sources (Google Trends, Amazon).
