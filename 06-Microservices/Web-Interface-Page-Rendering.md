---
title: Page Rendering & UI Styling Specification
type: protocol
status: active
microservice: web-interface
tags:
- '#service/web-interface'
- '#domain/web'
- '#type/protocol'
- '#state/active'
- '#zone/3-fleet'
- '#ai/ignore'
---
# 🎨 Page Rendering & UI Styling Specification: Bastien UI

This document formalizes the design system, typography scale, CSS tokens, and rendering rules for templates served inside the `web-interface` dashboard and micro-frontends registered via OpenMFE.

---

## 1. Visual Identity & Design Principles

The Bastien UI is designed to feel modern, high-tech, and highly readable. It avoids plain, harsh colors (pure blacks, pure whites) in favor of rich, low-fatigue, balanced tones.

### 🎨 Theme & Contrast Strategy
*   **Default Theme**: Dark Mode is the primary application theme. It utilizes **deep blue-gray tones** (`hsl(222, 25%, 10%)`) for backgrounds to soften the contrast against text, preventing eye strain.
*   **Light Theme**: Bright but soft **warm gray-white tones** (`hsl(210, 15%, 93%)`) to prevent the screen from being blindingly white.
*   **Contrast Control**: Never pair pure white text with pure black backgrounds or vice-versa. Always use semantic text color variables (`var(--color-text-primary)`, `var(--color-text-secondary)`).
*   **Glassmorphism**: Glass-like panels (`.bastien-card--glass`) with slight transparencies, background blurs (`backdrop-filter`), and thin borders are preferred for main dashboards and controls.

---

## 2. Typography Rules

Typography uses specific font stacks and sizing scales to establish a clear hierarchy.

### 🔤 Font Stacks and Roles

We use three semantic font families defined in `web/static/lib/tokens/design-tokens.css`:

1.  **Display & Headings** (`var(--font-display)`): `Outfit`
    *   **Usage**: Main page titles, dashboard sections, card titles, big metric numbers (KPI stats).
    *   **Weights**: `700` (Bold) or `600` (Semi-Bold) for headings; `400` (Regular) for secondary titles.
2.  **Body & Controls** (`var(--font-sans)`): `Inter`
    *   **Usage**: General paragraph descriptions, form labels, sidebar menu links, buttons, instructions, and standard text.
    *   **Weights**: `400` (Regular) for paragraphs/normal text; `500` (Medium) / `600` (Semi-Bold) for UI buttons and active menus.
3.  **Data & Monospace** (`var(--font-mono)`): `Fira Code`, `JetBrains Mono`, `Courier New`
    *   **Usage**: Numerical values (table columns, price ladders, bids/asks, order volumes), input fields, tickers, timestamps, logs, and python/script codes.
    *   **Weights**: `400` (Regular) for data lists, logs, and codes; `600` (Semi-Bold) for best prices or critical indicators.

> [!IMPORTANT]
> All numerical metrics (prices, volumes, depth) **MUST** use `var(--font-mono)` to guarantee tabular alignment and prevent layout shifting on real-time data updates.

### 📏 Typography Scale
All font sizes must use relative units (`rem`) bound to the layout scale:
*   `--font-size-2xs`: `0.625rem` (10px) — Small tags, secondary indicators.
*   `--font-size-xs`: `0.75rem` (12px) — Labels, helper texts, table headers.
*   `--font-size-sm`: `0.875rem` (14px) — Table rows, menus, sidebars, buttons.
*   `--font-size-base`: `1rem` (16px) — Standard body text.
*   `--font-size-lg`: `1.125rem` (18px) — Card sub-headers, small metrics.
*   `--font-size-xl`: `1.25rem` (20px) — Section titles.
*   `--font-size-2xl`: `1.5rem` (24px) — Page titles.
*   `--font-size-3xl`: `1.875rem` (30px) — Dashboard metrics.
*   `--font-size-4xl`: `2.25rem` (36px) — Large statistics.

---

### 🤖 AI Agent Typography Compliance
When writing or refactoring HTML/CSS code, AI agents must adhere to the following rules:
1.  **Never hardcode raw font family names**: Always use CSS variables (`var(--font-display)`, `var(--font-sans)`, `var(--font-mono)`).
2.  **Verify font context**: 
    *   If you are outputting a number, a ticker symbol (e.g. `ETHUSDT`), or a timestamp, wrap it in a container styled with `font-family: var(--font-mono)`.
    *   If you are writing a title/header, use `font-family: var(--font-display)`.
    *   If you are writing form descriptions or buttons, use `font-family: var(--font-sans)`.
3.  **Never use absolute font sizes**: Use the size scale CSS variables (e.g., `font-size: var(--font-size-sm)`). Do not write inline styles like `font-size: 14px;` or `font-size: 0.85rem;` unless referencing a variable.
4.  **Align text according to type**: Monospaced numerical values should be right-aligned or centered inside data tables.

---

## 3. Colors & Design Tokens (HSL System)

All colors are defined inside `web/static/lib/tokens/design-tokens.css` (with light theme overrides in `web/static/lib/theme/themes.css`). **Never use hardcoded hex or RGB colors.**

### Semantic Color Variables
*   `var(--color-bg-primary)`: Primary container backdrop.
*   `var(--color-bg-secondary)`: Sidebar / secondary panels.
*   `var(--color-bg-surface)`: Cards / module bodies.
*   `var(--color-bg-main)`: The content frame backdrop.
*   `var(--color-text-primary)`: High-contrast primary reading text.
*   `var(--color-text-secondary)`: Medium-contrast secondary text.
*   `var(--color-text-muted)`: Low-contrast labels or inactive states.
*   `var(--color-accent-primary)`: Primary brand color (sleek high-tech blue).
*   `var(--color-accent-success)`: Green for active, positive, connected, or up-trends.
*   `var(--color-accent-warning)`: Amber/yellow for warning, loading, or pending states.
*   `var(--color-accent-danger)`: Red for error, disconnected, or down-trends.

---

## 4. Layout Grid Specification

All pages must fit cleanly into the overall layout framework without causing overflow or layout shifts.

### 🧱 HTML Template Structure
To ensure design inheritance, child HTML templates served inside Go routes **MUST NOT** include boilerplate wraps:
*   ❌ **DO NOT USE**: `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`, or `<header>`.
*   ❌ **DO NOT DUPLICATE**: Bootstrap CDNs, Font Awesome CDN stylesheets, Google Fonts imports, or global scripts. These are already preloaded in the parent wrapper.
*   Every template must declare its scope inside the `"content"` define block:

```html
{{define "content"}}
<div class="bastien-container">
    <!-- Page grid row structures -->
    <div class="row">
        <div class="col-lg-12">
            <!-- Glassmorphic panel -->
        </div>
    </div>
</div>
{{end}}
```

### 🎛️ Page Title Headers
The main layout `base.html` automatically renders the title and description header segment dynamically.
*   Child templates **should not** define `<div class="bastien-page-header">` blocks to avoid double headings.
*   If a template specifically needs to override or remove the title segment, it can define an empty block:
    ```html
    {{define "page_header"}}{{end}}
    ```

### 📱 Responsive Behaviors
*   Use Bootstrap grid helper classes (`.row`, `.col-lg-X`, `.col-md-Y`, `.col-12`) to support dynamic column resizing down to mobile viewports.
*   The main content container (`.bastien-main`) should support multi-layered sidebar access. Opening sidebars must **not** blur or freeze interaction on desktop. 
*   Avoid adding close buttons directly inside local page content frames (the topbar handles triggers).

---

## 5. UI Component System

Use the predefined classes in `web/static/lib/components/components.css` to build interfaces.

### 🗂️ Cards & Glass Panels
Use the class `.bastien-card` or `.bastien-card--glass` for container structures:

```html
<div class="bastien-card bastien-card--glass">
    <div class="bastien-card__header">
        <span class="bastien-card__title">
            <i class="fa fa-sliders"></i> Config Editor
        </span>
    </div>
    <div class="bastien-card__body">
        <!-- Forms, metrics, tables -->
    </div>
</div>
```

### 📈 Metric Badges & Cards
For numerical KPIs, display them inside metric cards with trend indicators:

```html
<div class="bastien-metric-card">
    <div class="metric-header">
        <span class="metric-title">Traded Volume</span>
        <i class="fa fa-bar-chart metric-icon"></i>
    </div>
    <div class="metric-body">
        <span class="metric-value">4.52M</span>
        <span class="metric-trend trend-up">
            <i class="fa fa-arrow-up"></i> +12.3%
        </span>
    </div>
</div>
```

### 📊 Data Grids & Tables
Format lists and records using the `.bastien-datagrid` table wrappers for a modern, padded row representation:

```html
<div class="bastien-datagrid">
    <table>
        <thead>
            <tr>
                <th>Indicator</th>
                <th>Value</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>RSI</td>
                <td>58.2</td>
                <td><span class="bastien-badge bastien-badge--success">Oversold</span></td>
            </tr>
        </tbody>
    </table>
</div>
```

### 📝 Form Fields & Controls
Inputs, selections, and textareas must be styled using `.bastien-input`.

```html
<div class="bastien-form-group">
    <label class="bastien-form-group__label">Timeframe</label>
    <select class="bastien-input">
        <option>M1</option>
        <option>H1</option>
    </select>
</div>
```

### 🔘 Action Triggers
*   **Primary Button** (`.bastien-btn--primary`): For key operations (save, calculate, run).
*   **Secondary Button** (`.bastien-btn--secondary`): Glassmorphic button for secondary choices (cancel, clear, details).
*   **Danger Button** (`.bastien-btn--danger`): Red button for destructive or high-risk actions (delete, stop).

---

## 6. Icon Standards (Font Awesome)

The interface relies on **Font Awesome v4.7** (`fa fa-*`). Always include a meaningful icon to guide user actions.

### 📌 Icon Mapping Guide
*   `fa-terminal` / `fa-code`: Code inputs, developer tools, console outputs.
*   `fa-cogs` / `fa-sliders`: Configuration sections, control parameters.
*   `fa-bar-chart` / `fa-line-chart` / `fa-area-chart`: Quantitative metrics, statistics, graphs.
*   `fa-bars` / `fa-chevron-right` / `fa-chevron-down`: Navigation controls, toggle menus.
*   `fa-moon-o` / `fa-sun-o`: Theme toggling.
*   `fa-refresh` / `fa-spinner fa-spin`: Loading indicators, refresh handlers.
*   `fa-user` / `fa-lock`: Connect/disconnect operations, profile, login pages.
*   `fa-check-circle` / `fa-times-circle`: Positive connections, errors, operation status.
*   `fa-database` / `fa-folder-open`: Local files, databases, data logs.

---
*Back-links: [[Web-Interface-Hub]], [[Web-Interface-Integration-Protocol]], [[OpenMFE-Integration-Protocol]]*
