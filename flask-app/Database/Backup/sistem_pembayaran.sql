-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 30, 2022 at 06:00 PM
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
-- Table structure for table `pembayaran`
--

CREATE TABLE `pembayaran` (
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
-- Table structure for table `siswa`
--

CREATE TABLE `siswa` (
  `nis` varchar(9) NOT NULL,
  `nisn` varchar(20) NOT NULL,
  `tingkat` varchar(5) NOT NULL,
  `nama_siswa` varchar(200) NOT NULL,
  `status` varchar(50) NOT NULL,
  `kelas` varchar(2) NOT NULL,
  `jenis_kelamin` varchar(9) NOT NULL,
  `foto_path` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `siswa`
--

INSERT INTO `siswa` (`nis`, `nisn`, `tingkat`, `nama_siswa`, `status`, `kelas`, `jenis_kelamin`, `foto_path`) VALUES
('202107001', '', 'SMP', 'Abiyu Ahmad Zahran', 'Adik Kakak', '9D', 'Laki-laki', ''),
('202107002', '', 'SMP', 'Adley Ghaisan Poetra Kurniawan', 'Yatim', '9D', 'Laki-laki', ''),
('202107003', '', 'SMP', 'Akhdan Syafi Athallah', 'Reguler', '9D', 'Laki-laki', ''),
('202107004', '', 'SMP', 'Albert Eka Saputra', 'Adik Kakak', '9D', 'Laki-laki', ''),
('202107005', '', 'SMP', 'Anggata Alhaadi Ramadhan', 'Reguler', '9D', 'Laki-laki', ''),
('202107006', '', 'SMP', 'Bagas Al Fathir Danendra', 'Alumni', '9D', 'Laki-laki', ''),
('202107007', '', 'SMP', 'Daffa Amru Fadhila', 'Reguler', '9D', 'Laki-laki', ''),
('202107008', '', 'SMP', 'Danton Davinto Damaswara Putra', 'Adik Kakak', '9D', 'Laki-laki', ''),
('202107009', '', 'SMP', 'Disya Putra Kasyafi', 'Reguler', '9D', 'Laki-laki', ''),
('202107010', '', 'SMP', 'Fahri Dwi Rizki', 'Anak Pegawai', '9D', 'Laki-laki', ''),
('202107011', '', 'SMP', 'Fayruz Bintang Ali Pramono', 'Reguler', '9D', 'Laki-laki', ''),
('202107012', '', 'SMP', 'Hanif Abdurrahman', 'Reguler', '9D', 'Laki-laki', ''),
('202107013', '', 'SMP', 'Ibrahimavel Mohammad', 'Reguler', '9D', 'Laki-laki', ''),
('202107015', '', 'SMP', 'Mochammad Fierhand Ghazy', 'Adik Kakak', '9D', 'Laki-laki', ''),
('202107016', '', 'SMP', 'Mohammad Rally Deanandra Elfahreza ', 'Reguler', '9D', 'Laki-laki', ''),
('202107017', '', 'SMP', 'Muhamad Ihya Ulumuddin', 'Reguler', '9D', 'Laki-laki', ''),
('202107018', '', 'SMP', 'Muhammad Brian Riadi', 'Reguler', '9D', 'Laki-laki', ''),
('202107019', '', 'SMP', 'Muhammad Davin Attalah', 'Reguler', '9D', 'Laki-laki', ''),
('202107020', '', 'SMP', 'Muhammad Yatsrib Shadiqah Mulk', 'Inklusi', '9D', 'Laki-laki', ''),
('202107021', '', 'SMP', 'Najwan Muammar Zhariif', 'Alumni', '9D', 'Laki-laki', ''),
('202107022', '', 'SMP', 'Nur Athar Zaidan Dien Putra', 'Alumni', '9D', 'Laki-laki', ''),
('202107023', '', 'SMP', 'Panji Prayoga', 'Reguler', '9D', 'Laki-laki', ''),
('202107024', '', 'SMP', 'Rasya Dwi Erlangga Budiarso', 'Reguler', '9D', 'Laki-laki', ''),
('202107025', '', 'SMP', 'Riefqi Fathurrohman ', 'Reguler', '9D', 'Laki-laki', ''),
('202107026', '', 'SMP', 'Shandy Akbar Nugraha', 'Adik Kakak', '9D', 'Laki-laki', ''),
('202107027', '', 'SMP', 'Zhafran Fathir Muttaqin', 'Alumni', '9D', 'Laki-laki', ''),
('202107028', '', 'SMP', 'Aisyah Van Orleans', 'Reguler', '9J', 'Perempuan', ''),
('202107029', '', 'SMP', 'Alya Putri Karisa', 'Reguler', '9J', 'Perempuan', ''),
('202107030', '', 'SMP', 'Aziza Zuha Rifa', 'Alumni', '9J', 'Perempuan', ''),
('202107031', '', 'SMP', 'Daviena Az Zahra', 'Alumni', '9J', 'Perempuan', ''),
('202107032', '', 'SMP', 'Dinda Prameswari Putri Sekarayu', 'Reguler', '9J', 'Perempuan', ''),
('202107033', '', 'SMP', 'Dini Aulia Pratiwi', 'Reguler', '9J', 'Perempuan', ''),
('202107034', '', 'SMP', 'Frisiati Amni', 'Reguler', '9J', 'Perempuan', ''),
('202107035', '', 'SMP', 'Gwenza Netanya Suntawibowo', 'Reguler', '9J', 'Perempuan', ''),
('202107036', '', 'SMP', 'Keira Lucretia Aisha', 'Reguler', '9J', 'Perempuan', ''),
('202107037', '', 'SMP', 'Keysa Sabrina Sofyan', 'Reguler', '9J', 'Perempuan', ''),
('202107038', '', 'SMP', 'Kiarra Aleka Putri', 'Adik Kakak', '9J', 'Perempuan', ''),
('202107040', '', 'SMP', 'Marsya Farica', 'Alumni', '9J', 'Perempuan', ''),
('202107041', '', 'SMP', 'Najma Nuzula Eluwanish Hadiyan', 'Adik Kakak', '9J', 'Perempuan', ''),
('202107042', '', 'SMP', 'Nayla Farha Jannati', 'Reguler', '9J', 'Perempuan', ''),
('202107043', '', 'SMP', 'Nisrina Elvina Azalia', 'Adik Kakak', '9J', 'Perempuan', ''),
('202107044', '', 'SMP', 'Putri Qonita Rafifa Fitri', 'Reguler', '9J', 'Perempuan', ''),
('202107045', '', 'SMP', 'Qurrotaa\' Yuni Salsabila', 'Reguler', '9J', 'Perempuan', ''),
('202107046', '', 'SMP', 'Raisya Nairandy Tomigolung', 'Reguler', '9J', 'Perempuan', ''),
('202107047', '', 'SMP', 'Rasheesa Fitria Nuraini', 'Adik Kakak', '9J', 'Perempuan', ''),
('202107048', '', 'SMP', 'Renaisha Azzahra Nayla Aryo Putri', 'Reguler', '9J', 'Perempuan', ''),
('202107050', '', 'SMP', 'Sierra Al Karammy Dewanti', 'Reguler', '9J', 'Perempuan', ''),
('202107051', '', 'SMP', 'Siti Zhuraya Kamyra', 'Yayasan', '9J', 'Perempuan', ''),
('202107052', '', 'SMP', 'Syarifatul Mona', 'Reguler', '9J', 'Perempuan', ''),
('202107053', '', 'SMP', 'Tata Kirana Widyanto', 'Adik Kakak', '9J', 'Perempuan', ''),
('202107054', '', 'SMP', 'Zahira Ratnadhita', 'Reguler', '9J', 'Perempuan', ''),
('202107055', '', 'SMP', 'Zahra Aliya Putri Mulyasari', 'Alumni', '9J', 'Perempuan', ''),
('202107056', '', 'SMP', 'Aisyah Zashika Darmawijaya', 'Adik kakak', '9I', 'Perempuan', ''),
('202107057', '', 'SMP', 'Aisyah Zhafirah Amaliah', 'Alumni', '9I', 'Perempuan', ''),
('202107058', '', 'SMP', 'Aliya Ghassani Nadhira Fathania', 'Reguler', '9I', 'Perempuan', ''),
('202107059', '', 'SMP', 'Aprillia Fourtuna Larasati', 'Alumni', '9I', 'Perempuan', ''),
('202107060', '', 'SMP', 'Arifa Nafi\'ah Ulya', 'Anak Guru', '9I', 'Perempuan', ''),
('202107061', '', 'SMP', 'Attaira Tabina Nailah', 'Alumni', '9I', 'Perempuan', ''),
('202107062', '', 'SMP', 'Aurelia Amanda Ashila', 'Alumni', '9I', 'Perempuan', ''),
('202107063', '', 'SMP', 'Azka Putri Rahmansyah', 'Alumni', '9I', 'Perempuan', ''),
('202107064', '', 'SMP', 'Insanadilla Salafina Hidayat', 'Reguler', '9I', 'Perempuan', ''),
('202107065', '', 'SMP', 'Jihan Yumna Zakira', 'Reguler', '9I', 'Perempuan', ''),
('202107066', '', 'SMP', 'Kannaya Celia Putri', 'Alumni', '9I', 'Perempuan', ''),
('202107067', '', 'SMP', 'Keyla Anandita Khoirunnisa', 'Reguler', '9I', 'Perempuan', ''),
('202107068', '', 'SMP', 'Keysha Afra Aurellia', 'Reguler', '9I', 'Perempuan', ''),
('202107069', '', 'SMP', 'Marsha Azzahra Ridagiya', 'Reguler', '9I', 'Perempuan', ''),
('202107070', '', 'SMP', 'Nadhira Adya Pramesty', 'Reguler', '9I', 'Perempuan', ''),
('202107071', '', 'SMP', 'Nadia Rafadesta Janitra', 'Reguler', '9I', 'Perempuan', ''),
('202107072', '', 'SMP', 'Nashita Kayana Ritya', 'Reguler', '9I', 'Perempuan', ''),
('202107073', '', 'SMP', 'Neysa Calluela Dhiya Achmad', 'Adik kakak', '9I', 'Perempuan', ''),
('202107074', '', 'SMP', 'Nur Najmi Nuha Chamsyah Sutandi', 'Alumni', '9I', 'Perempuan', ''),
('202107075', '', 'SMP', 'Putri Anggia', 'Reguler', '9I', 'Perempuan', ''),
('202107076', '', 'SMP', 'Raisa Dini Fazila', 'Reguler', '9I', 'Perempuan', ''),
('202107077', '', 'SMP', 'Revina Aulia', 'Reguler', '9I', 'Perempuan', ''),
('202107078', '', 'SMP', 'Sabrina Asfa Azzahra', 'Reguler', '9I', 'Perempuan', ''),
('202107079', '', 'SMP', 'Salma Aura Maharani Igraha', 'Reguler', '9I', 'Perempuan', ''),
('202107080', '', 'SMP', 'Syifa Fauziah', 'Reguler', '9I', 'Perempuan', ''),
('202107081', '', 'SMP', 'Tadzkia Sukma Aulia', 'Reguler', '9I', 'Perempuan', ''),
('202107082', '', 'SMP', 'Tiara Meylina Tahir', 'Reguler', '9I', 'Perempuan', ''),
('202107083', '', 'SMP', 'Titra Alzena Thahira Masya', 'Reguler', '9I', 'Perempuan', ''),
('202107084', '', 'SMP', 'Aelan Alfadly Noreen Yulio', 'Reguler', '9P', 'Laki-laki', ''),
('202107085', '', 'SMP', 'Aldivo Langit Zulfian', 'Reguler', '9P', 'Laki-laki', ''),
('202107086', '', 'SMP', 'Allbie Avicenna', 'Yatim', '9P', 'Laki-laki', ''),
('202107087', '', 'SMP', 'Byantara Natha Gandi', 'Reguler', '9P', 'Laki-laki', ''),
('202107088', '', 'SMP', 'Chiqo Ahmad Bimo Umbara', 'Reguler', '9P', 'Laki-laki', ''),
('202107089', '', 'SMP', 'Dafi Hasyid Danurhadi', 'Alumni', '9P', 'Laki-laki', ''),
('202107090', '', 'SMP', 'Damar Wijaksono Persada', 'Alumni', '9P', 'Laki-laki', ''),
('202107091', '', 'SMP', 'Febi Ihsanul Azmi', 'Reguler', '9P', 'Laki-laki', ''),
('202107092', '', 'SMP', 'Ghazwan Rizqi Hanifan', 'Reguler', '9P', 'Laki-laki', ''),
('202107093', '', 'SMP', 'Hutomo Aryodifa', 'Alumni', '9P', 'Laki-laki', ''),
('202107094', '', 'SMP', 'Javier Darryl Al Aziz', 'Reguler', '9P', 'Laki-laki', ''),
('202107095', '', 'SMP', 'Lanang Fajar Anugrah', 'Reguler', '9P', 'Laki-laki', ''),
('202107096', '', 'SMP', 'Muhammad Afrizal', 'Yatim', '9P', 'Laki-laki', ''),
('202107097', '', 'SMP', 'Muhammad Ahdanil Hakim', 'Reguler', '9P', 'Laki-laki', ''),
('202107098', '', 'SMP', 'Muhammad Daniel', 'Alumni', '9P', 'Laki-laki', ''),
('202107100', '', 'SMP', 'Muhammad Farras Syathir Pryanda', 'Reguler', '9P', 'Laki-laki', ''),
('202107101', '', 'SMP', 'Muhammad Raffy Pasha', 'Reguler', '9P', 'Laki-laki', ''),
('202107102', '', 'SMP', 'Muhammad Razanavi Wahid', 'Reguler', '9P', 'Laki-laki', ''),
('202107103', '', 'SMP', 'Muhammad Suttan Akasyah', 'Reguler', '9P', 'Laki-laki', ''),
('202107104', '', 'SMP', 'Nail Huwaidi Dawwas', 'Reguler', '9P', 'Laki-laki', ''),
('202107105', '', 'SMP', 'Naufal Rifqiy Pratama', 'Adik Kakak', '9P', 'Laki-laki', ''),
('202107106', '', 'SMP', 'Putra Yusuf Dasa Perdana', 'Reguler', '9P', 'Laki-laki', ''),
('202107108', '', 'SMP', 'Rafi Adiguna Rosidin', 'Inklusi', '9P', 'Laki-laki', ''),
('202107109', '', 'SMP', 'Rizkia Reva Febryan', 'Reguler', '9P', 'Laki-laki', ''),
('202107110', '', 'SMP', 'Shaquil Fattah Alchair', 'Alumni', '9P', 'Laki-laki', ''),
('212207001', '', 'SMP', 'Amir Zaky Sali', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207002', '', 'SMP', 'Andika Dava Febrian', 'Reguler', '8D', 'Laki-laki', ''),
('212207003', '', 'SMP', 'Arafi Wahyu Permadani', 'Reguler', '8D', 'Laki-laki', ''),
('212207004', '', 'SMP', 'Arka Muhammad Shalih', 'Reguler', '8D', 'Laki-laki', ''),
('212207005', '', 'SMP', 'Bagas Julian Yudistira', 'Inklusi', '8D', 'Laki-laki', ''),
('212207006', '', 'SMP', 'Batara Altafaris Nugroho', 'Alumni', '8D', 'Laki-laki', ''),
('212207007', '', 'SMP', 'Daffa Nabel Naffisa Miyari', 'Alumni', '8D', 'Laki-laki', ''),
('212207008', '', 'SMP', 'Darrel Arvi Kalani', 'Alumni', '8D', 'Laki-laki', ''),
('212207009', '', 'SMP', 'Elsan Muhammad Urianfarrell', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207010', '', 'SMP', 'Fabian Magantis Wiranatakusumah', 'Alumni', '8D', 'Laki-laki', ''),
('212207011', '', 'SMP', 'Fadlan Aidan', 'Reguler', '8D', 'Laki-laki', ''),
('212207012', '', 'SMP', 'Faiz Hirzi Alfredo', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207013', '', 'SMP', 'Fathan Al-Maisan Rabbani', 'Alumni', '8D', 'Laki-laki', ''),
('212207014', '', 'SMP', 'Felix Aria Indrajit', 'Alumni', '8D', 'Laki-laki', ''),
('212207015', '', 'SMP', 'Gagas Ridho Utama', 'Alumni', '8D', 'Laki-laki', ''),
('212207016', '', 'SMP', 'Ghifari Aldima Rizqi', 'Reguler', '8D', 'Laki-laki', ''),
('212207017', '', 'SMP', 'Hanung Rasendrya Krisyanto', 'Alumni', '8D', 'Laki-laki', ''),
('212207018', '', 'SMP', 'Irsyal Afdhalus Haqi', 'Alumni', '8D', 'Laki-laki', ''),
('212207019', '', 'SMP', 'Marco Aydin Hylmi Iskandar', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207020', '', 'SMP', 'Muhammad Affan Raya Moefti', 'Alumni', '8D', 'Laki-laki', ''),
('212207021', '', 'SMP', 'Muhammad Aqila Gamiel Ramadhan', 'Alumni', '8D', 'Laki-laki', ''),
('212207022', '', 'SMP', 'Muhammad Fadel Ath Thoriq', 'Reguler', '8D', 'Laki-laki', ''),
('212207023', '', 'SMP', 'Muhammad Fattah Nugraha', 'Reguler', '8D', 'Laki-laki', ''),
('212207024', '', 'SMP', 'Muhammad Raihan Fathin', 'Alumni', '8D', 'Laki-laki', ''),
('212207025', '', 'SMP', 'Nasywaan Dzaki Muyassar', 'Yatim', '8D', 'Laki-laki', ''),
('212207026', '', 'SMP', 'Naufal Rafi Gunawan', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207027', '', 'SMP', 'Raden Nabeel Jusuf Gazali', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207028', '', 'SMP', 'Rafa Athaya', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207029', '', 'SMP', 'Rafif Asyraf', 'Adik Kakak', '8D', 'Laki-laki', ''),
('212207030', '', 'SMP', 'Zaidaan Faraz Qordhowi', 'Reguler', '8D', 'Laki-laki', ''),
('212207031', '', 'SMP', 'Alya Atifa Edfianti', 'Alumni', '8J', 'Perempuan', ''),
('212207032', '', 'SMP', 'Andisa Zahra Asari', 'Reguler', '8J', 'Perempuan', ''),
('212207033', '', 'SMP', 'Aulia Kanza Rahmadianti', 'Reguler', '8J', 'Perempuan', ''),
('212207034', '', 'SMP', 'Calysta Jelita Putri Hidayat', 'Reguler', '8J', 'Perempuan', ''),
('212207035', '', 'SMP', 'Cek Saffa Callysta Aisyahana', 'Adik Kakak', '8J', 'Perempuan', ''),
('212207036', '', 'SMP', 'Charity Mahdiyyah Aji', 'Alumni', '8J', 'Perempuan', ''),
('212207037', '', 'SMP', 'Fathia Karissa Naya', 'Reguler', '8J', 'Perempuan', ''),
('212207038', '', 'SMP', 'Kaila Malila Liko', 'Reguler', '8J', 'Perempuan', ''),
('212207039', '', 'SMP', 'Kanaya Naila Azhairine', 'Reguler', '8J', 'Perempuan', ''),
('212207040', '', 'SMP', 'Kania Zahra Azalia', 'Reguler', '8J', 'Perempuan', ''),
('212207041', '', 'SMP', 'Kayla Maritza Adyanugra', 'Reguler', '8J', 'Perempuan', ''),
('212207042', '', 'SMP', 'Kayyisah Nafiah Haddysan', 'Alumni', '8J', 'Perempuan', ''),
('212207043', '', 'SMP', 'Keisha Anindyta Kirana', 'Reguler', '8J', 'Perempuan', ''),
('212207044', '', 'SMP', 'Laura Risqa Ramadania', 'Alumni', '8J', 'Perempuan', ''),
('212207045', '', 'SMP', 'Manikhara Putri Mustofa', 'Alumni', '8J', 'Perempuan', ''),
('212207046', '', 'SMP', 'Maritza Azkia Putri', 'Alumni', '8J', 'Perempuan', ''),
('212207047', '', 'SMP', 'Nada Izzati Qonita', 'Alumni', '8J', 'Perempuan', ''),
('212207048', '', 'SMP', 'Nagita Azkia Salsabila', 'Alumni', '8J', 'Perempuan', ''),
('212207049', '', 'SMP', 'Nandya Rahel Nurhaliza', 'Adik Kakak', '8J', 'Perempuan', ''),
('212207050', '', 'SMP', 'Nayla Humaira', 'Adik Kakak', '8J', 'Perempuan', ''),
('212207051', '', 'SMP', 'Neisha Arinta Putri Sarjana', 'Alumni', '8J', 'Perempuan', ''),
('212207052', '', 'SMP', 'Neisya Syafina Rizkia Rusliyadi', 'Reguler', '8J', 'Perempuan', ''),
('212207053', '', 'SMP', 'Puti Rania Andressa', 'Alumni', '8J', 'Perempuan', ''),
('212207054', '', 'SMP', 'Qiara Alia Putri', 'Reguler', '8J', 'Perempuan', ''),
('212207055', '', 'SMP', 'Raissa Mufida Dzikri', 'Alumni', '8J', 'Perempuan', ''),
('212207056', '', 'SMP', 'Rania Al Yaasin Putri Santoso', 'Reguler', '8J', 'Perempuan', ''),
('212207057', '', 'SMP', 'Salshabila Roselani', 'Reguler', '8J', 'Perempuan', ''),
('212207058', '', 'SMP', 'Talitha Faiha Laksana', 'Alumni', '8J', 'Perempuan', ''),
('212207059', '', 'SMP', 'Zahra Syakria', 'Reguler', '8J', 'Perempuan', ''),
('212207060', '', 'SMP', 'Zahrani As Syifa', 'Adik Kakak', '8J', 'Perempuan', ''),
('212207061', '', 'SMP', 'Adara Maritza Sefin', 'Reguler', '8I', 'Perempuan', ''),
('212207062', '', 'SMP', 'Adara Permatasari', 'Alumni', '8I', 'Perempuan', ''),
('212207063', '', 'SMP', 'Aira Nur Annisa Herlambang', 'Reguler', '8I', 'Perempuan', ''),
('212207064', '', 'SMP', 'Aisyah Nur Izzah', 'Reguler', '8I', 'Perempuan', ''),
('212207065', '', 'SMP', 'Arsyla Nafizha Ayu', 'Reguler', '8I', 'Perempuan', ''),
('212207066', '', 'SMP', 'Aura Cahyaningtyas', 'Alumni', '8I', 'Perempuan', ''),
('212207067', '', 'SMP', 'Aydina Fakhira', 'Alumni', '8I', 'Perempuan', ''),
('212207068', '', 'SMP', 'Aysya Diva Adrianov', 'Reguler', '8I', 'Perempuan', ''),
('212207069', '', 'SMP', 'Bulan Rimba Ramadhani', 'Reguler', '8I', 'Perempuan', ''),
('212207070', '', 'SMP', 'Dyandra Alleta Fauzan', 'Reguler', '8I', 'Perempuan', ''),
('212207071', '', 'SMP', 'Elfarana Najla', 'Anak Guru', '8I', 'Perempuan', ''),
('212207072', '', 'SMP', 'Hafidhia Hasnaisha', 'Reguler', '8I', 'Perempuan', ''),
('212207073', '', 'SMP', 'Hasumi Faiha', 'Reguler', '8I', 'Perempuan', ''),
('212207074', '', 'SMP', 'Haurishafa Mutiara Sani', 'Reguler', '8I', 'Perempuan', ''),
('212207075', '', 'SMP', 'Kaila Maritza Tifani', 'Alumni', '8I', 'Perempuan', ''),
('212207076', '', 'SMP', 'Keysa Nurul Fadillah', 'Reguler', '8I', 'Perempuan', ''),
('212207077', '', 'SMP', 'Manayra Zavier Ali', 'Reguler', '8I', 'Perempuan', ''),
('212207078', '', 'SMP', 'Maritza Indri Nugraheni', 'Reguler', '8I', 'Perempuan', ''),
('212207079', '', 'SMP', 'Nadia Shafira', 'Adik Kakak', '8I', 'Perempuan', ''),
('212207080', '', 'SMP', 'Nadian Putri Syafina', 'Reguler', '8I', 'Perempuan', ''),
('212207081', '', 'SMP', 'Najwaa Irene Praba Waranggani', 'Reguler', '8I', 'Perempuan', ''),
('212207082', '', 'SMP', 'Nazhera Irba Iwel', 'Alumni', '8I', 'Perempuan', ''),
('212207083', '', 'SMP', 'Queen Sayyida Althaf Berutu', 'Reguler', '8I', 'Perempuan', ''),
('212207084', '', 'SMP', 'Sabika Zaura Khumairo', 'Adik Kakak', '8I', 'Perempuan', ''),
('212207085', '', 'SMP', 'Shazia Durrotul Hikmah', 'Alumni', '8I', 'Perempuan', ''),
('212207086', '', 'SMP', 'Talita Azka Aqilla', 'Reguler', '8I', 'Perempuan', ''),
('212207087', '', 'SMP', 'Tauja Faida', 'Anak Guru', '8I', 'Perempuan', ''),
('212207088', '', 'SMP', 'Tiara Kanza', 'Reguler', '8I', 'Perempuan', ''),
('212207089', '', 'SMP', 'Xena Aisyah Nadia', 'Alumni', '8I', 'Perempuan', ''),
('212207090', '', 'SMP', 'Zahra Aulia Rahma Putri Hendri', 'Alumni', '8I', 'Perempuan', ''),
('212207091', '', 'SMP', 'Abrarrais Haldisto Nugroho', 'Adik Kakak', '8P', 'Laki-laki', ''),
('212207092', '', 'SMP', 'Aizar Luthfi Khairan.A', 'Adik Kakak', '8P', 'Laki-laki', ''),
('212207093', '', 'SMP', 'Akmal Latif Khalifah', 'Alumni', '8P', 'Laki-laki', ''),
('212207094', '', 'SMP', 'Arief Alamsyah Suhadi', 'Yatim', '8P', 'Laki-laki', ''),
('212207095', '', 'SMP', 'Arjuna Nathabayu', 'Reguler', '8P', 'Laki-laki', ''),
('212207096', '', 'SMP', 'Attala Andafino', 'Reguler', '8P', 'Laki-laki', ''),
('212207097', '', 'SMP', 'Bintang Bhanu Pratama', 'Reguler', '8P', 'Laki-laki', ''),
('212207098', '', 'SMP', 'Farel Rizki Hariyanto', 'Alumni', '8P', 'Laki-laki', ''),
('212207099', '', 'SMP', 'Farrel Azka Eka Putra Mardala', 'Alumni', '8P', 'Laki-laki', ''),
('212207100', '', 'SMP', 'Fatih Hafizuddin Amhar', 'Alumni', '8P', 'Laki-laki', ''),
('212207101', '', 'SMP', 'Ghaisan Barra Hakim', 'Reguler', '8P', 'Laki-laki', ''),
('212207102', '', 'SMP', 'Hafiizh Yoga Barata', 'Reguler', '8P', 'Laki-laki', ''),
('212207103', '', 'SMP', 'Hafizh Hans Attallah', 'Reguler', '8P', 'Laki-laki', ''),
('212207104', '', 'SMP', 'Haikal Raditya Putra', 'Reguler', '8P', 'Laki-laki', ''),
('212207105', '', 'SMP', 'Keivan Fadillah Muhammad', 'Alumni', '8P', 'Laki-laki', ''),
('212207106', '', 'SMP', 'Muhammad Afnan Fayza Djamil', 'Reguler', '8P', 'Laki-laki', ''),
('212207107', '', 'SMP', 'Muhammad Almer Afkar Asy\'ari', 'Reguler', '8P', 'Laki-laki', ''),
('212207108', '', 'SMP', 'Muhammad Ammaar Fadhiil', 'Alumni', '8P', 'Laki-laki', ''),
('212207109', '', 'SMP', 'Muhammad Ammar Firdaus Putra', 'Reguler', '8P', 'Laki-laki', ''),
('212207110', '', 'SMP', 'Muhammad Fadhil Muchtar', 'Alumni', '8P', 'Laki-laki', ''),
('212207111', '', 'SMP', 'Muhammad Fadhil Rizki', 'Reguler', '8P', 'Laki-laki', ''),
('212207112', '', 'SMP', 'Muhammad Fairuz Safa Alzena', 'Alumni', '8P', 'Laki-laki', ''),
('212207113', '', 'SMP', 'Muhammad Hafizh Habibullah', 'Adik Kakak', '8P', 'Laki-laki', ''),
('212207114', '', 'SMP', 'Muhammad Hakeem Fairuzy', 'Reguler', '8P', 'Laki-laki', ''),
('212207115', '', 'SMP', 'Muhammad Royyan', 'Anak Guru', '8P', 'Laki-laki', ''),
('212207116', '', 'SMP', 'Nabil Taufiqurrahman', 'Reguler', '8P', 'Laki-laki', ''),
('212207117', '', 'SMP', 'Naufal Rafifaydin Fajriansyah', 'Adik Kakak', '8P', 'Laki-laki', ''),
('212207118', '', 'SMP', 'Razqa Ramadhan Sofyan', 'Adik Kakak', '8P', 'Laki-laki', ''),
('212207119', '', 'SMP', 'Shaquille Banu Sampurna', 'Reguler', '8P', 'Laki-laki', ''),
('212208120', '', 'SMP', 'Farrasah Nurul Avisa', 'Reguler', '9J', 'Perempuan', ''),
('212208121', '', 'SMP', 'Farry Hauzan Kairussyarief', 'Inklusi', '9D', 'Laki-laki', ''),
('212208122', '', 'SMP', 'Awabin Danish Nabeel Khusthar', 'Reguler', '9P', 'Laki-laki', '');

-- --------------------------------------------------------

--
-- Table structure for table `tagihan`
--

CREATE TABLE `tagihan` (
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
-- Indexes for table `pembayaran`
--
ALTER TABLE `pembayaran`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nis_pembayaran_sd` (`nis`);

--
-- Indexes for table `siswa`
--
ALTER TABLE `siswa`
  ADD PRIMARY KEY (`nis`);

--
-- Indexes for table `tagihan`
--
ALTER TABLE `tagihan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nis_tagihan_sd` (`nis`);

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
-- AUTO_INCREMENT for table `pembayaran`
--
ALTER TABLE `pembayaran`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tagihan`
--
ALTER TABLE `tagihan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_nip` FOREIGN KEY (`nip`) REFERENCES `pegawai` (`nip`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
