{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
module Paths_305construction (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/home/clement.auger/Module_Maths/305construction_2019/.stack-work/install/x86_64-linux-tinfo6/lts-14.14/8.6.5/bin"
libdir     = "/home/clement.auger/Module_Maths/305construction_2019/.stack-work/install/x86_64-linux-tinfo6/lts-14.14/8.6.5/lib/x86_64-linux-ghc-8.6.5/305construction-0.1.0.0-FwwJxO6o5zzHF5goz9J1eR-305construction-test"
dynlibdir  = "/home/clement.auger/Module_Maths/305construction_2019/.stack-work/install/x86_64-linux-tinfo6/lts-14.14/8.6.5/lib/x86_64-linux-ghc-8.6.5"
datadir    = "/home/clement.auger/Module_Maths/305construction_2019/.stack-work/install/x86_64-linux-tinfo6/lts-14.14/8.6.5/share/x86_64-linux-ghc-8.6.5/305construction-0.1.0.0"
libexecdir = "/home/clement.auger/Module_Maths/305construction_2019/.stack-work/install/x86_64-linux-tinfo6/lts-14.14/8.6.5/libexec/x86_64-linux-ghc-8.6.5/305construction-0.1.0.0"
sysconfdir = "/home/clement.auger/Module_Maths/305construction_2019/.stack-work/install/x86_64-linux-tinfo6/lts-14.14/8.6.5/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "305construction_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "305construction_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "305construction_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "305construction_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "305construction_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "305construction_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
