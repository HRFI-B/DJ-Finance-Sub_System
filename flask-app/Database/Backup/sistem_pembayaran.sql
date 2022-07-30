-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 30, 2022 at 04:50 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sistem_pembayaran`
--

-- --------------------------------------------------------

--
-- Table structure for table `biaya_spp_sd`
--

CREATE TABLE `biaya_spp_sd` (
  `id` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `biaya` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `biaya_spp_smp`
--

CREATE TABLE `biaya_spp_smp` (
  `id` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `biaya` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `biaya_spp_tk`
--

CREATE TABLE `biaya_spp_tk` (
  `id` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `biaya` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `biaya_tambahan_sd`
--

CREATE TABLE `biaya_tambahan_sd` (
  `id` int(11) NOT NULL,
  `katagori` varchar(50) NOT NULL,
  `biaya` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `biaya_tambahan_smp`
--

CREATE TABLE `biaya_tambahan_smp` (
  `id` int(11) NOT NULL,
  `katagori` int(50) NOT NULL,
  `biaya` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `biaya_tambahan_tk`
--

CREATE TABLE `biaya_tambahan_tk` (
  `id` int(11) NOT NULL,
  `katagori` varchar(50) NOT NULL,
  `biaya` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `pegawai`
--

CREATE TABLE `pegawai` (
  `nip` varchar(9) NOT NULL,
  `nama_pegawai` varchar(200) NOT NULL,
  `status` varchar(50) NOT NULL,
  `unit` varchar(100) NOT NULL,
  `jabatan` varchar(100) NOT NULL,
  `jenis_kelamin` varchar(9) NOT NULL,
  `foto_path` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pegawai`
--

INSERT INTO `pegawai` (`nip`, `nama_pegawai`, `status`, `unit`, `jabatan`, `jenis_kelamin`, `foto_path`) VALUES
('007100072', 'Muhammad Faiz Aiman Ghifarie', 'Tetap', 'Sekertariat', 'Kasubsie IT/SIM', 'Laki-laki', ''),
('01', 'Staff', 'Tetap', 'Sekertariat', 'Staff', 'Laki-laki', ''),
('119140008', 'Nurul Aulia Larasati', 'Magang', 'Sekertariat', 'Software Developer', 'Perempuan', ''),
('119140130', 'Ihza Fajrur Rachman Hasani', 'Magang', 'Sekertariat', 'Asisten Kasubsie IT/SIM', 'Laki-laki', 'WhatsApp Image 2022-07-06 at 8.46.36 AM.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `pembayaran_sd`
--

CREATE TABLE `pembayaran_sd` (
  `id` int(11) NOT NULL,
  `nis` varchar(9) NOT NULL,
  `pembayaran_periode_bulan` varchar(10) NOT NULL,
  `pembayaran_periode_ta` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `waktu_pembayaran` date NOT NULL,
  `spp` int(20) NOT NULL,
  `tabungan_wajib` int(20) NOT NULL,
  `katering` int(20) NOT NULL,
  `jemputan` int(20) NOT NULL,
  `ekskul` int(20) NOT NULL,
  `majelis_sekolah` int(20) NOT NULL,
  `kelas_berbakat` int(20) NOT NULL,
  `bimbel` int(20) NOT NULL,
  `total` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `pembayaran_smp`
--

CREATE TABLE `pembayaran_smp` (
  `id` int(11) NOT NULL,
  `nis` varchar(9) NOT NULL,
  `pembayaran_periode_bulan` varchar(10) NOT NULL,
  `pembayaran_periode_ta` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `waktu_pembayaran` date NOT NULL,
  `spp` int(20) NOT NULL,
  `tabungan_wajib` int(20) NOT NULL,
  `katering` int(20) NOT NULL,
  `jemputan` int(20) NOT NULL,
  `ekskul` int(20) NOT NULL,
  `majelis_sekolah` int(20) NOT NULL,
  `kelas_berbakat` int(20) NOT NULL,
  `bimbel` int(20) NOT NULL,
  `total` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `pembayaran_tk`
--

CREATE TABLE `pembayaran_tk` (
  `id` int(11) NOT NULL,
  `nis` varchar(9) NOT NULL,
  `pembayaran_periode_bulan` varchar(10) NOT NULL,
  `pembayaran_periode_ta` text NOT NULL,
  `status` int(20) NOT NULL,
  `waktu_pembayaran` date NOT NULL,
  `spp` int(20) NOT NULL,
  `tabungan_wajib` int(20) NOT NULL,
  `katering` int(20) NOT NULL,
  `jemputan` int(20) NOT NULL,
  `ekskul` int(20) NOT NULL,
  `majelis_sekolah` int(20) NOT NULL,
  `kelas_berbakat` int(20) NOT NULL,
  `bimbel` int(20) NOT NULL,
  `total` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `siswa_sd`
--

CREATE TABLE `siswa_sd` (
  `nis` varchar(9) NOT NULL,
  `nisn` varchar(20) NOT NULL,
  `nama_siswa` varchar(200) NOT NULL,
  `status` varchar(50) NOT NULL,
  `kelas` varchar(2) NOT NULL,
  `jenis_kelamin` varchar(9) NOT NULL,
  `foto_path` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `siswa_smp`
--

CREATE TABLE `siswa_smp` (
  `nis` varchar(9) NOT NULL,
  `nisn` varchar(20) NOT NULL,
  `nama_siswa` varchar(200) NOT NULL,
  `status` varchar(50) NOT NULL,
  `kelas` varchar(2) NOT NULL,
  `jenis_kelamin` varchar(9) NOT NULL,
  `foto_path` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `siswa_smp`
--

INSERT INTO `siswa_smp` (`nis`, `nisn`, `nama_siswa`, `status`, `kelas`, `jenis_kelamin`, `foto_path`) VALUES
('202107001', '', 'Abiyu Ahmad Zahran', 'Adik Kakak', '9D', 'Laki-laki', ''),
('202107002', '', 'Adley Ghaisan Poetra Kurniawan', 'Yatim', '9D', 'Laki-laki', ''),
('202107003', '', 'Akhdan Syafi Athallah', 'Reguler', '9D', 'Laki-laki', ''),
('202107004', '', 'Albert Eka Saputra', 'Adik Kakak', '9D', 'Laki-laki', ''),
('202107005', '', 'Anggata Alhaadi Ramadhan', 'Reguler', '9D', 'Laki-laki', ''),
('202107006', '', 'Bagas Al Fathir Danendra', 'Alumni', '9D', 'Laki-laki', ''),
('202107007', '', 'Daffa Amru Fadhila', 'Reguler', '9D', 'Laki-laki', ''),
('202107008', '', 'Danton Davinto Damaswara Putra', 'Adik Kakak', '9D', 'Laki-laki', ''),
('202107009', '', 'Disya Putra Kasyafi', 'Reguler', '9D', 'Laki-laki', ''),
('202107010', '', 'Fahri Dwi Rizki', 'Anak Pegawai', '9D', 'Laki-laki', ''),
('202107011', '', 'Fayruz Bintang Ali Pramono', 'Reguler', '9D', 'Laki-laki', ''),
('202107012', '', 'Hanif Abdurrahman', 'Reguler', '9D', 'Laki-laki', ''),
('202107013', '', 'Ibrahimavel Mohammad', 'Reguler', '9D', 'Laki-laki', ''),
('202107015', '', 'Mochammad Fierhand Ghazy', 'Adik Kakak', '9D', 'Laki-laki', ''),
('202107016', '', 'Mohammad Rally Deanandra Elfahreza ', 'Reguler', '9D', 'Laki-laki', ''),
('202107017', '', 'Muhamad Ihya Ulumuddin', 'Reguler', '9D', 'Laki-laki', ''),
('202107018', '', 'Muhammad Brian Riadi', 'Reguler', '9D', 'Laki-laki', ''),
('202107019', '', 'Muhammad Davin Attalah', 'Reguler', '9D', 'Laki-laki', ''),
('202107020', '', 'Muhammad Yatsrib Shadiqah Mulk', 'Inklusi', '9D', 'Laki-laki', ''),
('202107021', '', 'Najwan Muammar Zhariif', 'Alumni', '9D', 'Laki-laki', ''),
('202107022', '', 'Nur Athar Zaidan Dien Putra', 'Alumni', '9D', 'Laki-laki', ''),
('202107023', '', 'Panji Prayoga', 'Reguler', '9D', 'Laki-laki', ''),
('202107024', '', 'Rasya Dwi Erlangga Budiarso', 'Reguler', '9D', 'Laki-laki', ''),
('202107025', '', 'Riefqi Fathurrohman ', 'Reguler', '9D', 'Laki-laki', ''),
('202107026', '', 'Shandy Akbar Nugraha', 'Adik Kakak', '9D', 'Laki-laki', ''),
('202107027', '', 'Zhafran Fathir Muttaqin', 'Alumni', '9D', 'Laki-laki', ''),
('202107028', '', 'Aisyah Van Orleans', 'Reguler', '9J', 'Perempuan', ''),
('202107029', '', 'Alya Putri Karisa', 'Reguler', '9J', 'Perempuan', ''),
('202107030', '', 'Aziza Zuha Rifa', 'Alumni', '9J', 'Perempuan', ''),
('202107031', '', 'Daviena Az Zahra', 'Alumni', '9J', 'Perempuan', ''),
('202107032', '', 'Dinda Prameswari Putri Sekarayu', 'Reguler', '9J', 'Perempuan', ''),
('202107033', '', 'Dini Aulia Pratiwi', 'Reguler', '9J', 'Perempuan', ''),
('202107034', '', 'Frisiati Amni', 'Reguler', '9J', 'Perempuan', ''),
('202107035', '', 'Gwenza Netanya Suntawibowo', 'Reguler', '9J', 'Perempuan', ''),
('202107036', '', 'Keira Lucretia Aisha', 'Reguler', '9J', 'Perempuan', ''),
('202107037', '', 'Keysa Sabrina Sofyan', 'Reguler', '9J', 'Perempuan', ''),
('202107038', '', 'Kiarra Aleka Putri', 'Adik Kakak', '9J', 'Perempuan', ''),
('202107040', '', 'Marsya Farica', 'Alumni', '9J', 'Perempuan', ''),
('202107041', '', 'Najma Nuzula Eluwanish Hadiyan', 'Adik Kakak', '9J', 'Perempuan', ''),
('202107042', '', 'Nayla Farha Jannati', 'Reguler', '9J', 'Perempuan', ''),
('202107043', '', 'Nisrina Elvina Azalia', 'Adik Kakak', '9J', 'Perempuan', ''),
('202107044', '', 'Putri Qonita Rafifa Fitri', 'Reguler', '9J', 'Perempuan', ''),
('202107045', '', 'Qurrotaa\' Yuni Salsabila', 'Reguler', '9J', 'Perempuan', ''),
('202107046', '', 'Raisya Nairandy Tomigolung', 'Reguler', '9J', 'Perempuan', ''),
('202107047', '', 'Rasheesa Fitria Nuraini', 'Adik Kakak', '9J', 'Perempuan', ''),
('202107048', '', 'Renaisha Azzahra Nayla Aryo Putri', 'Reguler', '9J', 'Perempuan', ''),
('202107050', '', 'Sierra Al Karammy Dewanti', 'Reguler', '9J', 'Perempuan', ''),
('202107051', '', 'Siti Zhuraya Kamyra', 'Yayasan', '9J', 'Perempuan', ''),
('202107052', '', 'Syarifatul Mona', 'Reguler', '9J', 'Perempuan', ''),
('202107053', '', 'Tata Kirana Widyanto', 'Adik Kakak', '9J', 'Perempuan', ''),
('202107054', '', 'Zahira Ratnadhita', 'Reguler', '9J', 'Perempuan', ''),
('202107055', '', 'Zahra Aliya Putri Mulyasari', 'Alumni', '9J', 'Perempuan', ''),
('202107056', '', 'Aisyah Zashika Darmawijaya', 'Adik kakak', '9I', 'Perempuan', ''),
('202107057', '', 'Aisyah Zhafirah Amaliah', 'Alumni', '9I', 'Perempuan', ''),
('202107058', '', 'Aliya Ghassani Nadhira Fathania', 'Reguler', '9I', 'Perempuan', ''),
('202107059', '', 'Aprillia Fourtuna Larasati', 'Alumni', '9I', 'Perempuan', ''),
('202107060', '', 'Arifa Nafi\'ah Ulya', 'Anak Guru', '9I', 'Perempuan', ''),
('202107061', '', 'Attaira Tabina Nailah', 'Alumni', '9I', 'Perempuan', ''),
('202107062', '', 'Aurelia Amanda Ashila', 'Alumni', '9I', 'Perempuan', ''),
('202107063', '', 'Azka Putri Rahmansyah', 'Alumni', '9I', 'Perempuan', ''),
('202107064', '', 'Insanadilla Salafina Hidayat', 'Reguler', '9I', 'Perempuan', ''),
('202107065', '', 'Jihan Yumna Zakira', 'Reguler', '9I', 'Perempuan', ''),
('202107066', '', 'Kannaya Celia Putri', 'Alumni', '9I', 'Perempuan', ''),
('202107067', '', 'Keyla Anandita Khoirunnisa', 'Reguler', '9I', 'Perempuan', ''),
('202107068', '', 'Keysha Afra Aurellia', 'Reguler', '9I', 'Perempuan', ''),
('202107069', '', 'Marsha Azzahra Ridagiya', 'Reguler', '9I', 'Perempuan', ''),
('202107070', '', 'Nadhira Adya Pramesty', 'Reguler', '9I', 'Perempuan', ''),
('202107071', '', 'Nadia Rafadesta Janitra', 'Reguler', '9I', 'Perempuan', ''),
('202107072', '', 'Nashita Kayana Ritya', 'Reguler', '9I', 'Perempuan', ''),
('202107073', '', 'Neysa Calluela Dhiya Achmad', 'Adik kakak', '9I', 'Perempuan', ''),
('202107074', '', 'Nur Najmi Nuha Chamsyah Sutandi', 'Alumni', '9I', 'Perempuan', ''),
('202107075', '', 'Putri Anggia', 'Reguler', '9I', 'Perempuan', ''),
('202107076', '', 'Raisa Dini Fazila', 'Reguler', '9I', 'Perempuan', ''),
('202107077', '', 'Revina Aulia', 'Reguler', '9I', 'Perempuan', ''),
('202107078', '', 'Sabrina Asfa Azzahra', 'Reguler', '9I', 'Perempuan', ''),
('202107079', '', 'Salma Aura Maharani Igraha', 'Reguler', '9I', 'Perempuan', ''),
('202107080', '', 'Syifa Fauziah', 'Reguler', '9I', 'Perempuan', ''),
('202107081', '', 'Tadzkia Sukma Aulia', 'Reguler', '9I', 'Perempuan', ''),
('202107082', '', 'Tiara Meylina Tahir', 'Reguler', '9I', 'Perempuan', ''),
('202107083', '', 'Titra Alzena Thahira Masya', 'Reguler', '9I', 'Perempuan', ''),
('202107084', '', 'Aelan Alfadly Noreen Yulio', 'Reguler', '9P', 'Laki-laki', ''),
('202107085', '', 'Aldivo Langit Zulfian', 'Reguler', '9P', 'Laki-laki', ''),
('202107086', '', 'Allbie Avicenna', 'Yatim', '9P', 'Laki-laki', ''),
('202107087', '', 'Byantara Natha Gandi', 'Reguler', '9P', 'Laki-laki', ''),
('202107088', '', 'Chiqo Ahmad Bimo Umbara', 'Reguler', '9P', 'Laki-laki', ''),
('202107089', '', 'Dafi Hasyid Danurhadi', 'Alumni', '9P', 'Laki-laki', ''),
('202107090', '', 'Damar Wijaksono Persada', 'Alumni', '9P', 'Laki-laki', ''),
('202107091', '', 'Febi Ihsanul Azmi', 'Reguler', '9P', 'Laki-laki', ''),
('202107092', '', 'Ghazwan Rizqi Hanifan', 'Reguler', '9P', 'Laki-laki', ''),
('202107093', '', 'Hutomo Aryodifa', 'Alumni', '9P', 'Laki-laki', ''),
('202107094', '', 'Javier Darryl Al Aziz', 'Reguler', '9P', 'Laki-laki', ''),
('202107095', '', 'Lanang Fajar Anugrah', 'Reguler', '9P', 'Laki-laki', ''),
('202107096', '', 'Muhammad Afrizal', 'Yatim', '9P', 'Laki-laki', ''),
('202107097', '', 'Muhammad Ahdanil Hakim', 'Reguler', '9P', 'Laki-laki', ''),
('202107098', '', 'Muhammad Daniel', 'Alumni', '9P', 'Laki-laki', ''),
('202107100', '', 'Muhammad Farras Syathir Pryanda', 'Reguler', '9P', 'Laki-laki', ''),
('202107101', '', 'Muhammad Raffy Pasha', 'Reguler', '9P', 'Laki-laki', ''),
('202107102', '', 'Muhammad Razanavi Wahid', 'Reguler', '9P', 'Laki-laki', ''),
('202107103', '', 'Muhammad Suttan Akasyah', 'Reguler', '9P', 'Laki-laki', ''),
('202107104', '', 'Nail Huwaidi Dawwas', 'Reguler', '9P', 'Laki-laki', ''),
('202107105', '', 'Naufal Rifqiy Pratama', 'Adik Kakak', '9P', 'Laki-laki', ''),
('202107106', '', 'Putra Yusuf Dasa Perdana', 'Reguler', '9P', 'Laki-laki', ''),
('202107108', '', 'Rafi Adiguna Rosidin', 'Inklusi', '9P', 'Laki-laki', ''),
('202107109', '', 'Rizkia Reva Febryan', 'Reguler', '9P', 'Laki-laki', ''),
('202107110', '', 'Shaquil Fattah Alchair', 'Alumni', '9P', 'Laki-laki', ''),
('212207001', '', 'Amir Zaky Sali', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207002', '', 'Andika Dava Febrian', 'Reguler', '8D', 'Laki-laki', ''),
('212207003', '', 'Arafi Wahyu Permadani', 'Reguler', '8D', 'Laki-laki', ''),
('212207004', '', 'Arka Muhammad Shalih', 'Reguler', '8D', 'Laki-laki', ''),
('212207005', '', 'Bagas Julian Yudistira', 'Inklusi', '8D', 'Laki-laki', ''),
('212207006', '', 'Batara Altafaris Nugroho', 'Alumni', '8D', 'Laki-laki', ''),
('212207007', '', 'Daffa Nabel Naffisa Miyari', 'Alumni', '8D', 'Laki-laki', ''),
('212207008', '', 'Darrel Arvi Kalani', 'Alumni', '8D', 'Laki-laki', ''),
('212207009', '', 'Elsan Muhammad Urianfarrell', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207010', '', 'Fabian Magantis Wiranatakusumah', 'Alumni', '8D', 'Laki-laki', ''),
('212207011', '', 'Fadlan Aidan', 'Reguler', '8D', 'Laki-laki', ''),
('212207012', '', 'Faiz Hirzi Alfredo', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207013', '', 'Fathan Al-Maisan Rabbani', 'Alumni', '8D', 'Laki-laki', ''),
('212207014', '', 'Felix Aria Indrajit', 'Alumni', '8D', 'Laki-laki', ''),
('212207015', '', 'Gagas Ridho Utama', 'Alumni', '8D', 'Laki-laki', ''),
('212207016', '', 'Ghifari Aldima Rizqi', 'Reguler', '8D', 'Laki-laki', ''),
('212207017', '', 'Hanung Rasendrya Krisyanto', 'Alumni', '8D', 'Laki-laki', ''),
('212207018', '', 'Irsyal Afdhalus Haqi', 'Alumni', '8D', 'Laki-laki', ''),
('212207019', '', 'Marco Aydin Hylmi Iskandar', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207020', '', 'Muhammad Affan Raya Moefti', 'Alumni', '8D', 'Laki-laki', ''),
('212207021', '', 'Muhammad Aqila Gamiel Ramadhan', 'Alumni', '8D', 'Laki-laki', ''),
('212207022', '', 'Muhammad Fadel Ath Thoriq', 'Reguler', '8D', 'Laki-laki', ''),
('212207023', '', 'Muhammad Fattah Nugraha', 'Reguler', '8D', 'Laki-laki', ''),
('212207024', '', 'Muhammad Raihan Fathin', 'Alumni', '8D', 'Laki-laki', ''),
('212207025', '', 'Nasywaan Dzaki Muyassar', 'Yatim', '8D', 'Laki-laki', ''),
('212207026', '', 'Naufal Rafi Gunawan', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207027', '', 'Raden Nabeel Jusuf Gazali', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207028', '', 'Rafa Athaya', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207029', '', 'Rafif Asyraf', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207030', '', 'Zaidaan Faraz Qordhowi', 'Reguler', '8D', 'Laki-laki', ''),
('212207031', '', 'Alya Atifa Edfianti', 'Alumni', '8J', 'Perempuan', ''),
('212207032', '', 'Andisa Zahra Asari', 'Reguler', '8J', 'Perempuan', ''),
('212207033', '', 'Aulia Kanza Rahmadianti', 'Reguler', '8J', 'Perempuan', ''),
('212207034', '', 'Calysta Jelita Putri Hidayat', 'Reguler', '8J', 'Perempuan', ''),
('212207035', '', 'Cek Saffa Callysta Aisyahana', 'Adik Kakak', '8J', 'Perempuan', ''),
('212207036', '', 'Charity Mahdiyyah Aji', 'Alumni', '8J', 'Perempuan', ''),
('212207037', '', 'Fathia Karissa Naya', 'Reguler', '8J', 'Perempuan', ''),
('212207038', '', 'Kaila Malila Liko', 'Reguler', '8J', 'Perempuan', ''),
('212207039', '', 'Kanaya Naila Azhairine', 'Reguler', '8J', 'Perempuan', ''),
('212207040', '', 'Kania Zahra Azalia', 'Reguler', '8J', 'Perempuan', ''),
('212207041', '', 'Kayla Maritza Adyanugra', 'Reguler', '8J', 'Perempuan', ''),
('212207042', '', 'Kayyisah Nafiah Haddysan', 'Alumni', '8J', 'Perempuan', ''),
('212207043', '', 'Keisha Anindyta Kirana', 'Reguler', '8J', 'Perempuan', ''),
('212207044', '', 'Laura Risqa Ramadania', 'Alumni', '8J', 'Perempuan', ''),
('212207045', '', 'Manikhara Putri Mustofa', 'Alumni', '8J', 'Perempuan', ''),
('212207046', '', 'Maritza Azkia Putri', 'Alumni', '8J', 'Perempuan', ''),
('212207047', '', 'Nada Izzati Qonita', 'Alumni', '8J', 'Perempuan', ''),
('212207048', '', 'Nagita Azkia Salsabila', 'Alumni', '8J', 'Perempuan', ''),
('212207049', '', 'Nandya Rahel Nurhaliza', 'Adik Kakak', '8J', 'Perempuan', ''),
('212207050', '', 'Nayla Humaira', 'Adik Kakak', '8J', 'Perempuan', ''),
('212207051', '', 'Neisha Arinta Putri Sarjana', 'Alumni', '8J', 'Perempuan', ''),
('212207052', '', 'Neisya Syafina Rizkia Rusliyadi', 'Reguler', '8J', 'Perempuan', ''),
('212207053', '', 'Puti Rania Andressa', 'Alumni', '8J', 'Perempuan', ''),
('212207054', '', 'Qiara Alia Putri', 'Reguler', '8J', 'Perempuan', ''),
('212207055', '', 'Raissa Mufida Dzikri', 'Alumni', '8J', 'Perempuan', ''),
('212207056', '', 'Rania Al Yaasin Putri Santoso', 'Reguler', '8J', 'Perempuan', ''),
('212207057', '', 'Salshabila Roselani', 'Reguler', '8J', 'Perempuan', ''),
('212207058', '', 'Talitha Faiha Laksana', 'Alumni', '8J', 'Perempuan', ''),
('212207059', '', 'Zahra Syakria', 'Reguler', '8J', 'Perempuan', ''),
('212207060', '', 'Zahrani As Syifa', 'Adik Kakak', '8J', 'Perempuan', ''),
('212207061', '', 'Adara Maritza Sefin', 'Reguler', '8I', 'Perempuan', ''),
('212207062', '', 'Adara Permatasari', 'Alumni', '8I', 'Perempuan', ''),
('212207063', '', 'Aira Nur Annisa Herlambang', 'Reguler', '8I', 'Perempuan', ''),
('212207064', '', 'Aisyah Nur Izzah', 'Reguler', '8I', 'Perempuan', ''),
('212207065', '', 'Arsyla Nafizha Ayu', 'Reguler', '8I', 'Perempuan', ''),
('212207066', '', 'Aura Cahyaningtyas', 'Alumni', '8I', 'Perempuan', ''),
('212207067', '', 'Aydina Fakhira', 'Alumni', '8I', 'Perempuan', ''),
('212207068', '', 'Aysya Diva Adrianov', 'Reguler', '8I', 'Perempuan', ''),
('212207069', '', 'Bulan Rimba Ramadhani', 'Reguler', '8I', 'Perempuan', ''),
('212207070', '', 'Dyandra Alleta Fauzan', 'Reguler', '8I', 'Perempuan', ''),
('212207071', '', 'Elfarana Najla', 'Anak Guru', '8I', 'Perempuan', ''),
('212207072', '', 'Hafidhia Hasnaisha', 'Reguler', '8I', 'Perempuan', ''),
('212207073', '', 'Hasumi Faiha', 'Reguler', '8I', 'Perempuan', ''),
('212207074', '', 'Haurishafa Mutiara Sani', 'Reguler', '8I', 'Perempuan', ''),
('212207075', '', 'Kaila Maritza Tifani', 'Alumni', '8I', 'Perempuan', ''),
('212207076', '', 'Keysa Nurul Fadillah', 'Reguler', '8I', 'Perempuan', ''),
('212207077', '', 'Manayra Zavier Ali', 'Reguler', '8I', 'Perempuan', ''),
('212207078', '', 'Maritza Indri Nugraheni', 'Reguler', '8I', 'Perempuan', ''),
('212207079', '', 'Nadia Shafira', 'Adik Kakak', '8I', 'Perempuan', ''),
('212207080', '', 'Nadian Putri Syafina', 'Reguler', '8I', 'Perempuan', ''),
('212207081', '', 'Najwaa Irene Praba Waranggani', 'Reguler', '8I', 'Perempuan', ''),
('212207082', '', 'Nazhera Irba Iwel', 'Alumni', '8I', 'Perempuan', ''),
('212207083', '', 'Queen Sayyida Althaf Berutu', 'Reguler', '8I', 'Perempuan', ''),
('212207084', '', 'Sabika Zaura Khumairo', 'Adik Kakak', '8I', 'Perempuan', ''),
('212207085', '', 'Shazia Durrotul Hikmah', 'Alumni', '8I', 'Perempuan', ''),
('212207086', '', 'Talita Azka Aqilla', 'Reguler', '8I', 'Perempuan', ''),
('212207087', '', 'Tauja Faida', 'Anak Guru', '8I', 'Perempuan', ''),
('212207088', '', 'Tiara Kanza', 'Reguler', '8I', 'Perempuan', ''),
('212207089', '', 'Xena Aisyah Nadia', 'Alumni', '8I', 'Perempuan', ''),
('212207090', '', 'Zahra Aulia Rahma Putri Hendri', 'Alumni', '8I', 'Perempuan', ''),
('212207091', '', 'Abrarrais Haldisto Nugroho', 'Adik Kakak', '8P', 'Laki-laki', ''),
('212207092', '', 'Aizar Luthfi Khairan.A', 'Adik Kakak', '8P', 'Laki-laki', ''),
('212207093', '', 'Akmal Latif Khalifah', 'Alumni', '8P', 'Laki-laki', ''),
('212207094', '', 'Arief Alamsyah Suhadi', 'Yatim', '8P', 'Laki-laki', ''),
('212207095', '', 'Arjuna Nathabayu', 'Reguler', '8P', 'Laki-laki', ''),
('212207096', '', 'Attala Andafino', 'Reguler', '8P', 'Laki-laki', ''),
('212207097', '', 'Bintang Bhanu Pratama', 'Reguler', '8P', 'Laki-laki', ''),
('212207098', '', 'Farel Rizki Hariyanto', 'Alumni', '8P', 'Laki-laki', ''),
('212207099', '', 'Farrel Azka Eka Putra Mardala', 'Alumni', '8P', 'Laki-laki', ''),
('212207100', '', 'Fatih Hafizuddin Amhar', 'Alumni', '8P', 'Laki-laki', ''),
('212207101', '', 'Ghaisan Barra Hakim', 'Reguler', '8P', 'Laki-laki', ''),
('212207102', '', 'Hafiizh Yoga Barata', 'Reguler', '8P', 'Laki-laki', ''),
('212207103', '', 'Hafizh Hans Attallah', 'Reguler', '8P', 'Laki-laki', ''),
('212207104', '', 'Haikal Raditya Putra', 'Reguler', '8P', 'Laki-laki', ''),
('212207105', '', 'Keivan Fadillah Muhammad', 'Alumni', '8P', 'Laki-laki', ''),
('212207106', '', 'Muhammad Afnan Fayza Djamil', 'Reguler', '8P', 'Laki-laki', ''),
('212207107', '', 'Muhammad Almer Afkar Asy\'ari', 'Reguler', '8P', 'Laki-laki', ''),
('212207108', '', 'Muhammad Ammaar Fadhiil', 'Alumni', '8P', 'Laki-laki', ''),
('212207109', '', 'Muhammad Ammar Firdaus Putra', 'Reguler', '8P', 'Laki-laki', ''),
('212207110', '', 'Muhammad Fadhil Muchtar', 'Alumni', '8P', 'Laki-laki', ''),
('212207111', '', 'Muhammad Fadhil Rizki', 'Reguler', '8P', 'Laki-laki', ''),
('212207112', '', 'Muhammad Fairuz Safa Alzena', 'Alumni', '8P', 'Laki-laki', ''),
('212207113', '', 'Muhammad Hafizh Habibullah', 'Adik Kakak', '8P', 'Laki-laki', ''),
('212207114', '', 'Muhammad Hakeem Fairuzy', 'Reguler', '8P', 'Laki-laki', ''),
('212207115', '', 'Muhammad Royyan', 'Anak Guru', '8P', 'Laki-laki', ''),
('212207116', '', 'Nabil Taufiqurrahman', 'Reguler', '8P', 'Laki-laki', ''),
('212207117', '', 'Naufal Rafifaydin Fajriansyah', 'Adik Kakak', '8P', 'Laki-laki', ''),
('212207118', '', 'Razqa Ramadhan Sofyan', 'Adik Kakak', '8P', 'Laki-laki', ''),
('212207119', '', 'Shaquille Banu Sampurna', 'Reguler', '8P', 'Laki-laki', ''),
('212208120', '', 'Farrasah Nurul Avisa', 'Reguler', '9J', 'Perempuan', ''),
('212208121', '', 'Farry Hauzan Kairussyarief', 'Inklusi', '9D', 'Laki-laki', ''),
('212208122', '', 'Awabin Danish Nabeel Khusthar', 'Reguler', '9P', 'Laki-laki', '');

-- --------------------------------------------------------

--
-- Table structure for table `siswa_tk`
--

CREATE TABLE `siswa_tk` (
  `nis` varchar(9) NOT NULL,
  `nisn` varchar(20) NOT NULL,
  `nama_siswa` varchar(200) NOT NULL,
  `status` varchar(50) NOT NULL,
  `kelas` varchar(15) NOT NULL,
  `jenis_kelamin` varchar(9) NOT NULL,
  `foto_path` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tagihan_sd`
--

CREATE TABLE `tagihan_sd` (
  `id` int(11) NOT NULL,
  `nis` varchar(9) NOT NULL,
  `tagihan_bulan` int(2) NOT NULL,
  `jenis_tagihan` varchar(50) NOT NULL,
  `jumlah_tagihan` int(20) NOT NULL,
  `tagihan_tahun` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tagihan_smp`
--

CREATE TABLE `tagihan_smp` (
  `id` int(11) NOT NULL,
  `nis` varchar(9) NOT NULL,
  `tagihan_bulan` int(2) NOT NULL,
  `jenis_tagihan` varchar(50) NOT NULL,
  `jumlah_tagihan` int(20) NOT NULL,
  `tagihan_tahun` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tagihan_tk`
--

CREATE TABLE `tagihan_tk` (
  `id` int(11) NOT NULL,
  `nis` varchar(9) NOT NULL,
  `tagihan_bulan` int(2) NOT NULL,
  `jenis_tagihan` varchar(50) NOT NULL,
  `jumlah_tagihan` int(20) NOT NULL,
  `tagihan_tahun` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `password` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `otoritas` varchar(10) NOT NULL,
  `nip` varchar(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`, `otoritas`, `nip`) VALUES
('faiz.ganteng', 'Rahasia990803', 'Admin', '007100072'),
('ihza', '0', 'Admin', '119140130'),
('laras', '0', 'Admin', '119140008'),
('staff', 'staff123', 'Staff', '01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `biaya_spp_sd`
--
ALTER TABLE `biaya_spp_sd`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `biaya_spp_smp`
--
ALTER TABLE `biaya_spp_smp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `biaya_spp_tk`
--
ALTER TABLE `biaya_spp_tk`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `biaya_tambahan_sd`
--
ALTER TABLE `biaya_tambahan_sd`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `biaya_tambahan_smp`
--
ALTER TABLE `biaya_tambahan_smp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pegawai`
--
ALTER TABLE `pegawai`
  ADD PRIMARY KEY (`nip`);

--
-- Indexes for table `pembayaran_sd`
--
ALTER TABLE `pembayaran_sd`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nis_pembayaran_sd` (`nis`);

--
-- Indexes for table `pembayaran_smp`
--
ALTER TABLE `pembayaran_smp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nis_pembayaran_smp` (`nis`);

--
-- Indexes for table `pembayaran_tk`
--
ALTER TABLE `pembayaran_tk`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nis_pembayaran_tk` (`nis`);

--
-- Indexes for table `siswa_sd`
--
ALTER TABLE `siswa_sd`
  ADD PRIMARY KEY (`nis`);

--
-- Indexes for table `siswa_smp`
--
ALTER TABLE `siswa_smp`
  ADD PRIMARY KEY (`nis`);

--
-- Indexes for table `siswa_tk`
--
ALTER TABLE `siswa_tk`
  ADD PRIMARY KEY (`nis`);

--
-- Indexes for table `tagihan_sd`
--
ALTER TABLE `tagihan_sd`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nis_tagihan_sd` (`nis`);

--
-- Indexes for table `tagihan_smp`
--
ALTER TABLE `tagihan_smp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nis_tagihan_smp` (`nis`);

--
-- Indexes for table `tagihan_tk`
--
ALTER TABLE `tagihan_tk`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nis_tagihan_tk` (`nis`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`),
  ADD KEY `user_nip` (`nip`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `biaya_spp_sd`
--
ALTER TABLE `biaya_spp_sd`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `biaya_spp_smp`
--
ALTER TABLE `biaya_spp_smp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `biaya_spp_tk`
--
ALTER TABLE `biaya_spp_tk`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `biaya_tambahan_sd`
--
ALTER TABLE `biaya_tambahan_sd`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `biaya_tambahan_smp`
--
ALTER TABLE `biaya_tambahan_smp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pembayaran_sd`
--
ALTER TABLE `pembayaran_sd`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pembayaran_smp`
--
ALTER TABLE `pembayaran_smp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `pembayaran_tk`
--
ALTER TABLE `pembayaran_tk`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tagihan_sd`
--
ALTER TABLE `tagihan_sd`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tagihan_smp`
--
ALTER TABLE `tagihan_smp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tagihan_tk`
--
ALTER TABLE `tagihan_tk`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pembayaran_sd`
--
ALTER TABLE `pembayaran_sd`
  ADD CONSTRAINT `nis_pembayaran_sd` FOREIGN KEY (`nis`) REFERENCES `siswa_sd` (`nis`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `pembayaran_smp`
--
ALTER TABLE `pembayaran_smp`
  ADD CONSTRAINT `nis_pembayaran_smp` FOREIGN KEY (`nis`) REFERENCES `siswa_smp` (`nis`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `pembayaran_tk`
--
ALTER TABLE `pembayaran_tk`
  ADD CONSTRAINT `nis_pembayaran_tk` FOREIGN KEY (`nis`) REFERENCES `siswa_tk` (`nis`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tagihan_sd`
--
ALTER TABLE `tagihan_sd`
  ADD CONSTRAINT `nis_tagihan_sd` FOREIGN KEY (`nis`) REFERENCES `siswa_sd` (`nis`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tagihan_smp`
--
ALTER TABLE `tagihan_smp`
  ADD CONSTRAINT `nis_tagihan_smp` FOREIGN KEY (`nis`) REFERENCES `siswa_smp` (`nis`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tagihan_tk`
--
ALTER TABLE `tagihan_tk`
  ADD CONSTRAINT `nis_tagihan_tk` FOREIGN KEY (`nis`) REFERENCES `siswa_tk` (`nis`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_nip` FOREIGN KEY (`nip`) REFERENCES `pegawai` (`nip`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
