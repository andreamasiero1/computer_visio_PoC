# Project GuardIA / VisAi — Agent Guidelines & Domain Knowledge

## 📌 Project Overview
**GuardIA (VisAi)** is an AI-powered anti-theft and loss prevention system for fashion and retail environments based on Computer Vision and Edge AI processing.

---

## 🏛️ Architectural Principles & Domain Rules (Cascade Funnel)
The system utilizes a **Cascade Funnel** architecture to minimize edge computing load and eliminate false positives:

1. **GUI Dead Zones (Zone Morte):**
   - Structural areas where items remain static (racks, shelves, hangers) are marked deterministically via a GUI by store staff.
   - Zero AI compute overhead is wasted on structural scene understanding.
2. **No Shopping Baskets/Bags:**
   - Target retail stores do NOT use shopping baskets or shopping bags, eliminating the main cause of legitimate visual occlusion.
3. **Value / Dimension Filter:**
   - Tracking is strictly focused on medium/high-value apparel (> €40–50, e.g. jackets, hoodies, knitwear, trousers).
   - Small accessories (e.g. socks, belts) are filtered out to avoid visual noise.
4. **Entrance Exclusion:**
   - The store entrance is not a dead zone, preventing personal items carried by customers from triggering active tracking.

---

## ⚙️ The 5-Phase Sequential Flow

```
[ Raw Video Frame ]
       │
       ▼ (Fase 1: Preprocessing, Dead Zones Masking & Face Blur)
[ Active Non-Dead-Zone Pixels ]
       │
       ▼ (Fase 2: Person Detection & Spatial Context)
[ Person Bounding Boxes & Zones ]
       │
       ▼ (Fase 3: Capo Vivo Creation — Item removed from Dead Zone + Size Filter)
[ Active "Capo Vivo" Tracks ]
       │
       ▼ (Fase 4: Suspicious Gesture Recognition — Only on Person ∩ Capo Vivo ROI)
[ Suspicious Gesture Flag ]
       │
       ▼ (Fase 5: 10s Double Verification Timer)
[ CONFIRMED ALARM / STAFF ALERT ]
```

### Phase Details
- **Phase 1 (Frame Switching & Privacy by Design):**
  - Computational masking of dead zones (racks/shelves).
  - Immediate face blurring on input frames for strict GDPR and EU AI Act compliance.
- **Phase 2 (Person Detection):**
  - Person bounding box extraction and spatial mapping across store zones.
- **Phase 3 (Capo Vivo Identification):**
  - An apparel bounding box is labeled and tracked as **"Capo Vivo"** IF AND ONLY IF:
    1. It exceeds the size/value threshold.
    2. Its movement originates from a defined Dead Zone (e.g. pulled from a hanger).
  - Tracking is limited strictly to active Capi Vivi, not the hundreds of static garments in the store.
- **Phase 4 (Suspicious Gesture Recognition on Capo Vivo):**
  - Heavy AI models (Pose Estimation, Action Recognition, Kinematic Analysis) execute **ONLY** on the intersection of Person and Capo Vivo.
  - Detects suspicious arm/body movements (e.g. slipping the garment inside a jacket, pocket, or bag).
- **Phase 5 (10-Second Disappearance Validation Timer):**
  - Sequential validation step triggered only after Phase 4 flag.
  - If the Capo Vivo disappears from sight and **does NOT reappear within 10 seconds** with empty hands, concealment is confirmed.
  - If the item reappears within 10 seconds (innocuous body occlusion), the timer resets and the alert is canceled.

---

## 🧠 Boolean Alarm Logic

Final alarm / staff notification is triggered if and only if the temporal sequence satisfies:

```text
Allarme = (Esiste CapoVivo == TRUE) 
          AND (GestoSospetto Rilevato == TRUE) 
          AND (CapoVivo Ricomparso entro 10s == FALSE)
```

---

## 📚 Second Brain / LLM Wiki (`VisAi/`)
- Rules & schema: `VisAi/CLAUDE.md`
- Raw notes: `VisAi/raw/`
- Compiled wiki pages: `VisAi/wiki/` (sources, concepts, topics, meta)
