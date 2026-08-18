---
name: find-differences-image-generator
description: Generate a formal "Find the Differences" puzzle image consisting of two vertically stacked images with a small number of intentional differences.
---

# Find the Differences Image Generator

## Purpose

Generate a high-quality "Find the Differences" puzzle image.

The output must contain two nearly identical images placed vertically:

- Top Image → Original image
- Bottom Image → Modified version containing a few intentional differences

The puzzle should be enjoyable, visually clear, and suitable for all audiences.

---

# Image Layout

Generate a **single image** with the following specifications.

- Resolution: **1080 x 1350 pixels**
- Aspect Ratio: **4:5**
- Orientation: Portrait

Layout:

```
+--------------------------------------+
|                                      |
|          Original Image              |
|                                      |
+--------------------------------------+
|                                      |
|          Modified Image              |
|                                      |
+--------------------------------------+
```

- Original image occupies the upper half.
- Modified image occupies the lower half.
- Both images must have identical dimensions.
- Images must be perfectly aligned.
- No overlapping.
- Maintain equal spacing and margins.

---

# Theme Requirements

The generated scene must always be:

- Professional
- Formal
- Family-friendly
- Clean
- Non-offensive
- Non-political
- Non-religious
- Non-violent
- PNG Format

Examples include:

- Office workspace
- Meeting room
- Conference hall
- Reception area
- Business people
- Corporate desk
- Library
- Classroom
- Laboratory
- Airport lounge
- Hotel lobby
- University campus
- Coffee shop
- Park
- Museum

Avoid:

- Gore
- Violence
- Weapons
- Hate symbols
- Political campaigns
- Religious imagery
- Adult content
- Drugs
- Smoking
- Alcohol
- Gambling
- Scary imagery
- Copyrighted characters
- Brand logos
- Watermarks

---

# Differences

The bottom image must contain exactly **3–4 differences**.

Allowed modifications include:

- Remove an object
- Add an object
- Change object color
- Move an object slightly
- Rotate an object
- Change facial expression
- Change clothing color
- Open/close a door
- Turn monitor on/off
- Replace one object with another
- Change plant size
- Remove picture frame
- Add stationery item
- Change mug color
- Move chair
- Toggle lights
- Change wall clock time

Differences should be:

- Clearly visible
- Natural
- Spread across the image
- Independent of each other

Do NOT:

- Change the entire background
- Change camera angle
- Change lighting dramatically
- Change image style
- Add text labels
- Add arrows
- Circle differences
- Highlight differences

The player should discover them manually.

---

# Similarity Constraints

The two images should be approximately **98% identical**.

Keep identical:

- Camera angle
- Perspective
- Composition
- Lighting
- Shadows
- Characters
- Background
- Colors (except intentional changes)
- Art style

Only the intended differences should vary.

---

# Originality

Every generated puzzle must be unique.

Never intentionally recreate:

- Previous layouts
- Previous object arrangements
- Previous difference combinations
- Previous themes

Introduce variation through:

- Environment
- Furniture
- Characters
- Camera framing
- Decorations
- Object placement
- Time of day
- Seasonal décor

---

# Visual Quality

Generate images that are:

- High resolution
- Sharp
- Well-lit
- Realistic or high-quality digital illustration
- Consistent in style
- Rich in detail

Avoid:

- Blurry objects
- Distorted anatomy
- Cropped subjects
- Floating objects
- AI artifacts
- Duplicate objects unless intentional

---

# Difference Placement

Distribute differences across the image.

Example:

Difference 1 → Top left

Difference 2 → Center

Difference 3 → Bottom right

Difference 4 → Upper right

Avoid clustering all differences in one location.

---

# Difficulty

Target a **High** difficulty.

Differences should require observation but should not be impossible to detect.

---

# Output Requirements

Return **one combined image only**.

Do not output:

- Separate images
- Explanation
- Difference list
- Coordinates
- JSON
- Bounding boxes
- Captions
- Save the image in PNG format in /workspace/images/ path

The output should consist solely of the final puzzle image.

---

# Success Criteria

A successful puzzle satisfies all of the following:

- 1080 x 1350 resolution
- Portrait orientation
- Original image on top
- Modified image on bottom
- Exactly 3–4 differences
- Formal theme
- Family-friendly
- High visual quality
- Differences naturally integrated
- Images nearly identical
- Unique composition