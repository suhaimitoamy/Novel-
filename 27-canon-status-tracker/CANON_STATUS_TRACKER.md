# Canon Status Tracker

## Tujuan Dokumen

Dokumen ini adalah **tracker status canon** untuk seluruh repo *Kael Drayven: The Forsaken Heir*. Fungsinya adalah menjaga agar repo yang sudah besar ini tetap mudah dikelola: jelas mana yang sudah terkunci, mana yang masih fleksibel, mana yang sekadar contoh, dan mana yang butuh hati-hati kalau direvisi karena bisa merusak banyak lapisan lain.

Prinsip utamanya:

- Tidak semua dokumen punya tingkat kekuncian yang sama.
- Revisi tanpa tahu dampaknya bisa merusak konsistensi repo.
- Tracker ini dipakai untuk membantu keputusan revisi, bukan membekukan kreativitas.

---

# I. Status Key

## LOCKED CORE
Dokumen sudah dianggap fondasi kuat. Revisi masih mungkin, tetapi hanya kalau benar-benar perlu dan harus diikuti pengecekan silang ke banyak dokumen lain.

## STABLE CANON
Dokumen sudah sehat dan kuat. Masih boleh dipertajam, tetapi arah besarnya sebaiknya tidak diubah sembarangan.

## ACTIVE SUPPORT
Dokumen aktif menopang repo dan sangat berguna, tetapi masih lebih fleksibel untuk diperluas atau dipadatkan.

## EXECUTION FLEX
Dokumen lebih dekat ke tahap eksekusi. Isinya boleh direvisi lebih bebas selama tidak bertabrakan dengan canon inti.

## ARCHIVE / FUTURE
Dokumen atau ide yang belum jadi fokus canon utama, atau baru relevan untuk ekspansi berikutnya.

---

# II. Tracker per Dokumen

---

## `README.md`
**Status:** STABLE CANON  
**Fungsi:** pintu masuk repo  
**Risiko revisi:** rendah  
**Catatan:** boleh terus diperbarui untuk sinkronisasi struktur repo.

---

## `01-kael-canon/KAEL_CANON.md`
**Status:** LOCKED CORE  
**Fungsi:** fondasi protagonis  
**Risiko revisi:** sangat tinggi  
**Catatan:** perubahan di sini akan berdampak ke cast, world core, alur utama, revelation order, relationship matrix, dan seluruh season breakdown.

---

## `02-cast-core-canon/CAST_CORE_CANON.md`
**Status:** LOCKED CORE  
**Fungsi:** fondasi cast utama  
**Risiko revisi:** tinggi  
**Catatan:** revisi besar harus dicek ke relationship matrix, season breakdown, dan faction relations.

---

## `03-world-core-canon/WORLD_CORE_CANON.md`
**Status:** LOCKED CORE  
**Fungsi:** fondasi metafisika dan hukum dunia  
**Risiko revisi:** sangat tinggi  
**Catatan:** perubahan istilah atau hukum dasar akan merambat ke timeline, revelation order, faction relations, season breakdown, dan glossary.

---

## `04-alur-utama-canon/ALUR_UTAMA_CANON.md`
**Status:** LOCKED CORE  
**Fungsi:** tulang punggung cerita besar  
**Risiko revisi:** sangat tinggi  
**Catatan:** perubahan besar di sini harus diikuti audit ke volume/season structure dan season 1–8 breakdown.

---

## `05-organisasi-elit-antagonis/THE_ECLIPSED_COVENANT.md`
**Status:** STABLE CANON  
**Fungsi:** fondasi organisasi elit antagonis  
**Risiko revisi:** sedang-tinggi  
**Catatan:** aman dipertajam, tapi jangan menggeser fungsi inti Covenant tanpa cek Season 5–8 dan faction relations.

## `05-organisasi-elit-antagonis/SEATS_OF_THE_ECLIPSED_COVENANT.md`
**Status:** ACTIVE SUPPORT  
**Fungsi:** rincian struktur kursi Covenant  
**Risiko revisi:** sedang  
**Catatan:** masih bisa dipoles, ditambah, atau dipadatkan selama ideologi inti Covenant tetap konsisten.

---

## `06-empire-cast-canon/EMPIRE_CAST_CANON.md`
**Status:** STABLE CANON  
**Fungsi:** wajah geopolitik 12 kekaisaran  
**Risiko revisi:** sedang  
**Catatan:** detail wilayah masih cukup fleksibel, tapi nama besar dan fungsi naratif wilayah sebaiknya dijaga.

---

## `07-recurring-npc-network/RECURRING_NPC_NETWORK.md`
**Status:** ACTIVE SUPPORT  
**Fungsi:** denyut dunia kecil dan manusia biasa  
**Risiko revisi:** rendah-sedang  
**Catatan:** sangat aman diperluas, selama tidak mengubah prinsip dasar dunia hidup.

---

## `08-volume-season-structure/VOLUME_SEASON_STRUCTURE.md`
**Status:** LOCKED CORE  
**Fungsi:** struktur macro serial  
**Risiko revisi:** tinggi  
**Catatan:** semua season breakdown bergantung pada dokumen ini.

---

## `09-execution-standards/PROSE_AND_CHAPTER_STANDARDS.md`
**Status:** EXECUTION FLEX  
**Fungsi:** standar gaya dan kualitas prosa  
**Risiko revisi:** rendah  
**Catatan:** sangat aman dipertajam seiring masuk ke tahap drafting.

---

## `10-story-risks-and-fixes/STORY_RISKS_AND_FIXES.md`
**Status:** EXECUTION FLEX  
**Fungsi:** alat diagnosis titik lemah proyek  
**Risiko revisi:** rendah  
**Catatan:** dokumen ini justru sebaiknya hidup dan boleh di-update saat repo berkembang.

---

## `11-season-1-arc-breakdown/SEASON_1_ARC_BREAKDOWN.md`
**Status:** STABLE CANON  
**Fungsi:** breakdown konkret pembuka serial  
**Risiko revisi:** sedang  
**Catatan:** aman dipertajam, tetapi jangan mengubah fungsi besar Season 1 sembarangan.

---

## `12-scene-engine/SCENE_ENGINE_AND_BEAT_TEMPLATE.md`
**Status:** EXECUTION FLEX  
**Fungsi:** alat kerja adegan dan beat  
**Risiko revisi:** rendah  
**Catatan:** sangat fleksibel dan bisa terus disempurnakan.

---

## `13-canon-draft-chapters/CHAPTER_01_ASHES_BEFORE_THE_NAME.md`
**Status:** EXECUTION FLEX  
**Fungsi:** contoh prose canon awal  
**Risiko revisi:** rendah-sedang  
**Catatan:** contoh, bukan fondasi yang tak boleh disentuh.

## `13-canon-draft-chapters/CHAPTER_02_BRIGHT_CLOTH_ON_MUD.md`
**Status:** EXECUTION FLEX  
**Fungsi:** contoh prose canon awal  
**Risiko revisi:** rendah-sedang  
**Catatan:** aman direvisi bila nanti masuk drafting penuh.

## `13-canon-draft-chapters/CHAPTER_03_THE_ROOM_ABOVE_THE_ASH.md`
**Status:** EXECUTION FLEX  
**Fungsi:** contoh prose canon awal  
**Risiko revisi:** rendah-sedang  
**Catatan:** aman direvisi bila nanti masuk drafting penuh.

---

## `14-world-timeline-canon/WORLD_TIMELINE_CANON.md`
**Status:** LOCKED CORE  
**Fungsi:** kronologi sejarah dunia  
**Risiko revisi:** tinggi  
**Catatan:** perubahan di sini akan memengaruhi world core, revelation order, faction relations, dan season breakdown.

---

## `15-revelation-order/REVELATION_ORDER.md`
**Status:** LOCKED CORE  
**Fungsi:** urutan pengungkapan misteri  
**Risiko revisi:** tinggi  
**Catatan:** salah satu dokumen paling penting untuk menjaga pacing dan misteri. Jangan direvisi tanpa alasan kuat.

---

## `16-season-2-arc-breakdown/SEASON_2_ARC_BREAKDOWN.md`
**Status:** STABLE CANON  
**Fungsi:** breakdown Season 2  
**Risiko revisi:** sedang  
**Catatan:** boleh dipertajam, terutama detail tokoh dan titik tekan emosional.

## `17-season-3-arc-breakdown/SEASON_3_ARC_BREAKDOWN.md`
**Status:** STABLE CANON  
**Fungsi:** breakdown Season 3  
**Risiko revisi:** sedang  
**Catatan:** jaga agar fungsi Fragmen dan Rowan tidak bergeser sembarangan.

## `18-faction-relations-canon/FACTION_RELATIONS_CANON.md`
**Status:** STABLE CANON  
**Fungsi:** arsitektur hubungan antar blok dunia  
**Risiko revisi:** sedang-tinggi  
**Catatan:** revisi kecil aman; revisi besar harus cek world core, alur utama, dan season-season tengah.

## `19-season-4-arc-breakdown/SEASON_4_ARC_BREAKDOWN.md`
**Status:** STABLE CANON  
**Fungsi:** breakdown Season 4  
**Risiko revisi:** sedang  
**Catatan:** jaga keseimbangan antara politik, ideologi, dan emosi.

## `20-season-5-arc-breakdown/SEASON_5_ARC_BREAKDOWN.md`
**Status:** STABLE CANON  
**Fungsi:** breakdown Season 5  
**Risiko revisi:** sedang  
**Catatan:** jaga Covenant tetap tajam tapi tidak berlebihan.

## `21-season-6-arc-breakdown/SEASON_6_ARC_BREAKDOWN.md`
**Status:** STABLE CANON  
**Fungsi:** breakdown Season 6  
**Risiko revisi:** sedang  
**Catatan:** hati-hati menjaga perang tetap bermakna dan tidak kosong.

## `22-season-7-arc-breakdown/SEASON_7_ARC_BREAKDOWN.md`
**Status:** STABLE CANON  
**Fungsi:** breakdown Season 7  
**Risiko revisi:** sedang  
**Catatan:** jaga Malakar dan Fragmen tidak menelan fungsi relasi inti.

## `23-season-8-arc-breakdown/SEASON_8_ARC_BREAKDOWN.md`
**Status:** STABLE CANON  
**Fungsi:** breakdown Season 8 / ending  
**Risiko revisi:** tinggi  
**Catatan:** karena ini menentukan ending, revisinya harus sangat hati-hati dan dicek ke relationship matrix.

---

## `24-character-relationship-matrix/CHARACTER_RELATIONSHIP_MATRIX.md`
**Status:** LOCKED CORE  
**Fungsi:** arsitektur relasi emosi dan ideologi  
**Risiko revisi:** tinggi  
**Catatan:** perubahan besar di sini bisa mengubah rasa seluruh serial. Revisi harus sangat sadar fungsi tiap tokoh.

---

## `25-master-canon-index/MASTER_CANON_INDEX.md`
**Status:** ACTIVE SUPPORT  
**Fungsi:** peta induk repo  
**Risiko revisi:** rendah  
**Catatan:** boleh terus diperbarui seiring repo bertambah.

## `26-glossary-and-proper-noun-index/GLOSSARY_AND_PROPER_NOUN_INDEX.md`
**Status:** ACTIVE SUPPORT  
**Fungsi:** kamus istilah dan nama besar  
**Risiko revisi:** rendah-sedang  
**Catatan:** harus hidup dan terus diperbarui saat proper noun baru masuk.

## `27-canon-status-tracker/CANON_STATUS_TRACKER.md`
**Status:** ACTIVE SUPPORT  
**Fungsi:** tracker kesehatan dan tingkat kekuncian repo  
**Risiko revisi:** rendah  
**Catatan:** justru harus diperbarui seiring repo berkembang.

---

# III. Zona Paling Sensitif

Dokumen yang dianggap paling sensitif terhadap revisi besar:

1. `KAEL_CANON.md`
2. `WORLD_CORE_CANON.md`
3. `ALUR_UTAMA_CANON.md`
4. `VOLUME_SEASON_STRUCTURE.md`
5. `WORLD_TIMELINE_CANON.md`
6. `REVELATION_ORDER.md`
7. `CHARACTER_RELATIONSHIP_MATRIX.md`
8. `SEASON_8_ARC_BREAKDOWN.md`

Kalau salah satu dari dokumen ini berubah besar, audit silang hampir pasti diperlukan.

---

# IV. Zona Paling Fleksibel

Dokumen yang paling aman untuk diutak-atik saat masuk ke tahap pengembangan lanjut:

- `PROSE_AND_CHAPTER_STANDARDS.md`
- `STORY_RISKS_AND_FIXES.md`
- `SCENE_ENGINE_AND_BEAT_TEMPLATE.md`
- draft chapter contoh
- recurring NPC network
- glossary
- master index
- status tracker

---

# V. Workflow Revisi yang Disarankan

## Kalau revisi menyentuh protagonis
Cek:
- Kael canon
- cast core
- relationship matrix
- alur utama
- ending

## Kalau revisi menyentuh hukum dunia
Cek:
- world core
- timeline
- revelation order
- faction relations
- season tengah dan akhir

## Kalau revisi menyentuh musuh utama
Cek:
- Covenant docs
- faction relations
- season 5–8
- relationship matrix untuk Rowan / Malakar

## Kalau revisi menyentuh ending
Cek:
- Season 8 breakdown
- Kael canon
- relationship matrix
- alur utama
- volume/season structure

---

# VI. Health Snapshot Saat Ini

## Yang sudah sangat sehat
- protagonis
- cast inti
- world core
- timeline
- alur season 1–8
- revelation order
- faction relations
- relationship matrix

## Yang sehat dan siap dikembangkan
- empire cast
- recurring NPC
- Covenant seats detail
- chapter contoh awal
- execution docs

## Yang masih ideal untuk ekspansi masa depan
- lore appendix per wilayah
- glossary lebih rinci
- tracker versi draft per volume
- arc-to-chapter mapping rinci

---

# VII. Ringkasan Canon

**CANON_STATUS_TRACKER** menjaga repo *Kael Drayven: The Forsaken Heir* tetap terbaca sebagai sistem kerja yang hidup, bukan sekadar kumpulan dokumen bagus. Dengan tracker ini, jelas mana yang sudah terkunci kuat, mana yang masih fleksibel, mana yang aman diperluas, dan mana yang harus direvisi dengan sangat hati-hati. Ini penting agar makin besarnya repo tidak berubah menjadi kekacauan, tetapi tetap berkembang sebagai story bible yang disiplin, sehat, dan siap dipakai jangka panjang.
