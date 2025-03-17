# WebGPU Hashing Performance Demo

<img width="1282" alt="Screenshot 2025-03-17 at 2 08 08 PM" src="https://github.com/user-attachments/assets/9e5cb5e3-03a4-471e-ac31-ff0933daf2a6" />

A demo comparing SHA-256 performance on WebGPU and a CPU implementation. Both implementations process an array of `UInt8Array` inputs, hashing each element.

## Experiement

The experiment generates random string of size 32 and of count ranging from: $` 10^1, 10^2, 10^3, 10^4, 10^5, 2 * 10^5, 4 * 10^5, 6 * 10^5, 8 * 10^5 `$ and $` 10^6. `$

The runtimes of the CPU and GPU implementations are then logged and tagged with performance API. The results are also logged in the console to be easily copied.

## Quickstart

```bash
npm install
npm run sha
```

## References

- CPU SHA256 Implementation [https://github.com/emn178/js-sha256](https://github.com/emn178/js-sha256)
- WebGPU SHA256 Implementation [https://github.com/MarcoCiaramella/sha256-gpu/tree/main](https://github.com/MarcoCiaramella/sha256-gpu/tree/main)
- Inital inspiration and Matrix implementations [https://github.com/TalDerei/Web-Mining](https://github.com/TalDerei/Web-Mining)
