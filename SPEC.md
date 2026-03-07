# AI News Aggregator - Specification

## Project Overview
- **Project Name:** AI News Aggregator
- **Type:** Web Application (Flask + Python)
- **Core Functionality:** Aggregates AI news from top webzines, displays unified view with 3-4 articles per source
- **Target Users:** AI enthusiasts, researchers, developers

## Tech Stack
- Backend: Python/Flask
- Frontend: HTML/CSS/JavaScript (responsive, modern design)
- News Sources: RSS feeds from top AI webzines

## News Sources (6-7 sources)
1. **TechCrunch AI** - https://techcrunch.com/category/artificial-intelligence/feed/
2. **VentureBeat AI** - https://venturebeat.com/category/ai/feed/
3. **MIT Technology Review AI** - https://www.technologyreview.com/feed/topic/artificial-intelligence/
4. **OpenAI Blog** - https://openai.com/blog/rss.xml
5. **Google AI Blog** - https://blog.google/technology/ai/rss
6. **Anthropic Blog** - https://www.anthropic.com/rss
7. **Hugging Face Blog** - https://huggingface.co/blog/rss.xml

## UI/UX Specification

### Layout Structure
- **Header:** Logo, title, last updated timestamp
- **Main Content:** Grid of news source cards
- **Each Card:** Source name, 3-4 article items with title, date, link
- **Footer:** Refresh button, copyright

### Visual Design
- **Color Palette:**
  - Background: #0f0f0f (dark)
  - Cards: #1a1a1a
  - Accent: #00d4ff (cyan)
  - Secondary: #7c3aed (purple)
  - Text Primary: #ffffff
  - Text Secondary: #a0a0a0
- **Typography:** 
  - Headings: Inter Bold
  - Body: Inter Regular
  - Monospace for dates: JetBrains Mono
- **Spacing:** 24px card padding, 16px gap
- **Effects:** Subtle glow on cards, hover lift effect

### Responsive Breakpoints
- Mobile (<768px): Single column
- Tablet (768-1024px): 2 columns
- Desktop (>1024px): 3 columns

## Functionality
1. Fetch RSS feeds on page load (server-side)
2. Parse and extract article title, link, date
3. Display 3-4 most recent articles per source
4. Auto-refresh every 5 minutes
5. Manual refresh button
6. Show loading state while fetching

## Acceptance Criteria
- [x] All 7 RSS feeds fetch successfully
- [x] 3-4 articles displayed per source
- [x] Articles link to original sources (new tab)
- [x] Professional dark theme UI
- [x] Responsive on all devices
- [x] Last updated timestamp shown
- [x] Error handling for failed feeds
