-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2022 at 03:40 PM
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
('119140130', 'Ihza Fajrur Rachman Hasani', 'Magang', 'Sekertariat', 'Asisten IT Support', 'Laki-Laki', 'WhatsApp Image 2022-07-06 at 8.46.36 AM.jpeg'),
('31212', 'Bambang', 'Aktif', '', 'Other', 'Perempuan', 'MicrosoftTeams-image.png'),
('321976', 'Abdullah Mujib', 'Tidak Tetap', 'Sekertariat', '-', 'Laki-Laki', 'MicrosoftTeams-image (5).png');

-- --------------------------------------------------------

--
-- Table structure for table `pembayaran_sd`
--

CREATE TABLE `pembayaran_sd` (
  `id` int(11) NOT NULL,
  `nis` varchar(9) NOT NULL,
  `jumlah_pembayaran` int(20) NOT NULL,
  `pembayaran_bulan` int(2) NOT NULL,
  `status` varchar(20) NOT NULL,
  `waktu_pembayaran` date NOT NULL,
  `jenis_pembayaran` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `pembayaran_smp`
--

CREATE TABLE `pembayaran_smp` (
  `id` int(11) NOT NULL,
  `nis` varchar(9) NOT NULL,
  `jumlah_pembayaran` int(20) NOT NULL,
  `pembayaran_bulan` int(2) NOT NULL,
  `status` varchar(20) NOT NULL,
  `waktu_pembayaran` date NOT NULL,
  `jenis_pembayaran` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `pembayaran_tk`
--

CREATE TABLE `pembayaran_tk` (
  `id` int(11) NOT NULL,
  `nis` varchar(9) NOT NULL,
  `jumlah_pembayaran` int(20) NOT NULL,
  `pembayaran_bulan` int(2) NOT NULL,
  `status` int(20) NOT NULL,
  `waktu_pembayaran` date NOT NULL,
  `jenis_pembayaran` varchar(50) NOT NULL
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
('119140130', '0119140130', 'Ihza Fajrur Rachman Hasani', 'Yayasan', '7D', 'Laki-laki', '1549425553128.png');

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
('ihza', '0', 'Admin', '119140130');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

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
