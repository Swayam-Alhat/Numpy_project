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

# Image Contrast (Grayscale Image)

---

## 1. Brightness & Darkness (Simple)

- Each pixel has a value between **0 to 255**
- 0 = pure black, 255 = pure white
- To brighten → just **add** a value to every pixel
- To darken → just **subtract** a value from every pixel
- The **gap or difference between pixels stays the same**
- Only the overall intensity shifts up or down

---

## 2. What is Contrast?

Every pixel has a value between 0 to 255, where 128 is the mid-gray (the neutral center point of the scale). The core idea of contrast is that every pixel has a gap or distance from this mid-gray value (128), and contrast operation simply increases or decreases this gap.

```
128 - 60 = 68
```

This gap of 68 tells us how far this pixel is sitting from the center. Now, contrast is all about what we do with this gap — either stretch it (pixel moves further from 128, increasing contrast) or shrink it (pixel moves closer to 128, decreasing contrast).

Contrast means **how far pixels are from the middle gray value i.e 128.**

- 128 is the midpoint of 0-255 scale, which represents a neutral gray
- Every pixel has a **distance/gap from 128**
- Contrast operation either **increases or decreases this gap**

---

## 3. High Contrast (Pixels move AWAY from 128)

Dark pixels get darker, bright pixels get brighter.

**Example — Dark pixel:**

```
Original pixel value = 60
Gap from 128 = 128 - 60 = 68

After increasing contrast:
60 → 40 or 30  (moving further away from 128, becoming more dark)
New gap = 128 - 30 = 98  (gap increased from 68 to 98)
```

**Example — Bright pixel:**

```
Original pixel value = 190
Gap from 128 = 190 - 128 = 62

After increasing contrast:
190 → 230 or 240  (moving further away from 128, becoming more bright)
New gap = 240 - 128 = 112  (gap increased from 62 to 112)
```

So high contrast = gaps get bigger = darks get darker + brights get brighter.

---

## 4. Low Contrast (Pixels move CLOSER to 128)

Dark pixels become more gray, bright pixels become more gray.

**Example — Dark pixel:**

```
Original pixel value = 60
Gap from 128 = 128 - 60 = 68

After decreasing contrast:
60 → 90 or 100  (moving closer to 128, becoming more gray)
New gap = 128 - 90 = 38  (gap decreased from 68 to 38)
```

**Example — Bright pixel:**

```
Original pixel value = 190
Gap from 128 = 190 - 128 = 62

After decreasing contrast:
190 → 160 or 150  (moving closer to 128, becoming more gray)
New gap = 160 - 128 = 32  (gap decreased from 62 to 32)
```

So low contrast = gaps get smaller = everything pulls toward gray.

---

## 5. The Formula

```
output = 128 + (pixel - 128) * factor
```

**Breaking it down step by step:**

### Step 1 — `pixel - 128`

```
pixel = 60
60 - 128 = -68
```

This calculates the **gap/distance of the pixel from 128.**
Negative means the pixel is below 128 (dark side).
Positive means the pixel is above 128 (bright side).

### Step 2 — `* factor`

```
-68 * 1.5 = -102
```

This **scales the gap.**

- factor > 1 → gap gets bigger → high contrast
- factor < 1 → gap gets smaller → low contrast
- factor = 1 → gap stays same → no change
- factor = 0 → gap becomes 0 → everything turns gray (128)
- factor < 0 → gap flips → image inverts (dark becomes bright)

### Step 3 — `128 + result`

```
128 + (-102) = 26
```

This **brings the pixel back** to the correct position on the 0-255 scale.
The midpoint 128 is added back because we shifted it to 0 in Step 1.

---

## 6. Full Example Walkthrough

**Pixel = 60, Factor = 1.5 (increase contrast)**

```
Step 1: 60 - 128      = -68      (gap from 128)
Step 2: -68 * 1.5     = -102     (gap increased)
Step 3: 128 + (-102)  =  26      (final pixel value)
```

Original: 60 → Output: 26. Pixel moved further away from 128. Got darker. ✅

**Pixel = 190, Factor = 1.5 (increase contrast)**

```
Step 1: 190 - 128     =  62      (gap from 128)
Step 2:  62 * 1.5     =  93      (gap increased)
Step 3: 128 + 93      = 221      (final pixel value)
```

Original: 190 → Output: 221. Pixel moved further away from 128. Got brighter. ✅

**Pixel = 60, Factor = 0.5 (decrease contrast)**

```
Step 1: 60 - 128      = -68      (gap from 128)
Step 2: -68 * 0.5     = -34      (gap decreased)
Step 3: 128 + (-34)   =  94      (final pixel value)
```

Original: 60 → Output: 94. Pixel moved closer to 128. Became more gray. ✅

---

## 7. Key Takeaways

- Contrast = controlling the **gap/distance of each pixel from 128**
- The formula is just the **mathematical way to scale that gap**
- `pixel - 128` → finds the gap
- `* factor` → scales the gap
- `+ 128` → brings it back to correct scale
- This formula is applied to **every single pixel** in the image
- The midpoint pixel (128) **never changes** regardless of factor, because its gap is 0

---

# How Image Blurring Works (Grayscale Image)

For each pixel, we look at its surrounding neighbors (including itself), calculate their average value, and replace the pixel with that average. This creates a blur effect.

For pixels at the edge dont have complete neighbors as other pixels have. So create a padding around an array.

The higher the intensity, the bigger the neighborhood (5×5, 7×7...), so more pixels get mixed together -> stronger blur.

Read below code to understand how to blur an image.

```python
def blur_image():
    image_array = np.array(image,dtype=np.float32)

    # add padding of 1 width from all 4 sides
    padded_array = np.pad(image_array,pad_width=1,mode="constant",constant_values=0)

    rows,cols = padded_array.shape # 258,258

    result_data = []

    for i in range(1,rows - 1):
        result_row = []
        for j in range(1,cols - 1):
            sub_matrix = padded_array[i-1:i+2,j-1:j+2]
            avg = np.mean(sub_matrix)
            result_row.append(avg)

        result_data.append(result_row)

    result_array = np.array(result_data)

    result_image = Image.fromarray(result_array.astype(np.uint8))
    result_image.show()
```
