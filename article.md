**Week 1: Finite Field Elements, the math quietly powering blockchains**

A few weeks ago, I promised a public build challenge: we’d explore blockchain from the ground up in **Go**, week by week, sharing insights, code, and the intuition behind it all.

Here’s the first installment.

Before elliptic curves, digital signatures, or zero-knowledge proofs, blockchains rely on something much more fundamental: **finite fields**.

If this concept isn’t clear, cryptography feels like magic.
If it *is* clear, everything else starts to click.

---

### What is a finite field?

Think of a clock.

On a 12-hour clock:

* The numbers only go from 0 to 11
* 9 + 5 doesn’t give 14, it gives 2
* That’s modular arithmetic

A finite field works the same way, except:

* The “clock size” is a **prime number**
* Every non-zero number has an inverse
* Division is always possible

That last point is why primes matter so much in cryptography.

---

### Why blockchains care

Finite fields give us:

* Deterministic math
* No floating point errors
* No rounding ambiguity
* Guaranteed inverses (critical for signatures)

Elliptic curves, ECDSA, Schnorr, all of it is built on top of this.
If arithmetic isn’t perfectly predictable, cryptography collapses.

---

### What’s a field element?

A field element is just:

> a number that lives *inside* a finite field

So “7” and “7 mod 19” are **not the same thing** mathematically.

That’s exactly what my `FieldElement` type models: a value *plus* the field it belongs to.

---

### Why the code looks the way it does

By enforcing:

* values always stay within the field
* operations only happen between elements of the same field

we make invalid math impossible to ignore. Errors show up early instead of silently breaking cryptographic logic later. That’s intentional.

---

### What’s next

With finite fields in place, we’re ready to move up the stack:

* Elliptic curve points
* Point addition and scalar multiplication
* Digital signatures

Check out the full Go implementation here: [https://github.com/Caleb40/elliptic-curves-go](https://github.com/Caleb40/elliptic-curves-go)

This post is about understanding *why* the code exists, not just making it compile.


If you want the next post to dive into inverses or elliptic curves themselves, drop a comment 👇
