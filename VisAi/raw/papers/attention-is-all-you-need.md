# Attention Is All You Need

**Autori**: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin

**Pubblicato**: 12 giugno 2017 (NeurIPS 2017)

**URL**: https://arxiv.org/abs/1706.03762

## Abstract

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

## Punti chiave

### Il problema
I modelli dominanti per la traduzione automatica (e più in generale per la sequence transduction) si basavano su reti neurali ricorrenti (RNN) come LSTM e GRU. Queste architetture hanno un problema fondamentale: processano i token in sequenza, il che limita la parallelizzazione durante il training e rende difficile catturare dipendenze a lungo raggio.

### La soluzione: il Transformer
Il paper propone un'architettura completamente nuova chiamata **Transformer** che elimina completamente la ricorrenza e le convoluzioni, basandosi **esclusivamente su meccanismi di attenzione** (self-attention).

### Componenti chiave

1. **Self-Attention (Scaled Dot-Product Attention)**: ogni token nella sequenza può "guardare" tutti gli altri token contemporaneamente. L'attenzione è calcolata come:
   - `Attention(Q, K, V) = softmax(QK^T / √d_k) V`

2. **Multi-Head Attention**: invece di un singolo meccanismo di attenzione, il modello usa multiple "teste" parallele, ognuna che impara a prestare attenzione a diversi aspetti della rappresentazione.

3. **Positional Encoding**: dato che non c'è ricorrenza, l'informazione sulla posizione viene iniettata tramite encoding sinusoidali sommati agli embedding di input.

4. **Encoder-Decoder**: l'architettura mantiene la struttura encoder-decoder, ma sia encoder che decoder sono stack di layer identici basati su self-attention e feed-forward networks.

5. **Feed-Forward Networks**: ogni layer include una rete feed-forward applicata posizione per posizione, identica su tutte le posizioni.

### Risultati
- **WMT 2014 EN-DE**: 28.4 BLEU (nuovo SOTA, +2 BLEU sopra il miglior ensemble precedente)
- **WMT 2014 EN-FR**: 41.8 BLEU (nuovo SOTA single-model)
- **Training**: 3.5 giorni su 8 GPU — una frazione del costo dei modelli precedenti
- **Generalizzazione**: funziona bene anche su English constituency parsing

### Impatto
Il Transformer è diventato l'architettura fondamentale di praticamente tutti i modelli di linguaggio moderni: BERT, GPT, T5, PaLM, LLaMA, e ogni altro LLM. È probabilmente il paper più influente del deep learning degli ultimi 10 anni.
