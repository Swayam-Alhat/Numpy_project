# Learnings from project

### 1. np.array() vs np.asarray()

**np.array()** - Creates a new copy of image data. Use this when you want to manipulate the data.

**np.asarray()** - Creates a view of original data (no copy). Use this when you only want to analyze/read data. More memory efficient.

---

### 2. uint8 dtype

uint8 can only hold values from 0 to 255.

- If value exceeds 255, it wraps back to 0. So 255 + 1 = 0, 255 + 2 = 1 and so on.
- If value goes below 0, it wraps to 255. So 0 - 1 = 255, 0 - 2 = 254 and so on.

This is why we convert to int32 before manipulating — so values can go beyond 255 or below 0 without wrapping. After clipping, we convert back to uint8 because PIL's fromarray() expects uint8.  
**See function brighten_image in main.py**

---
