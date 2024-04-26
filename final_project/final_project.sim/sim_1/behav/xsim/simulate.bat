@echo off
REM ****************************************************************************
REM Vivado (TM) v2020.1 (64-bit)
REM
REM Filename    : simulate.bat
REM Simulator   : Xilinx Vivado Simulator
REM Description : Script for simulating the design by launching the simulator
REM
REM Generated by Vivado on Fri Apr 26 15:05:25 +0500 2024
REM SW Build 2902540 on Wed May 27 19:54:49 MDT 2020
REM
REM Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.
REM
REM usage: simulate.bat
REM
REM ****************************************************************************
echo "xsim tbHazard_behav -key {Behavioral:sim_1:Functional:tbHazard} -tclbatch tbHazard.tcl -view C:/Users/Dell/Documents/uni_docs/cs/computer architecture/final_project/final_project/testbench_RISCV_behav.wcfg -view C:/Users/Dell/Documents/uni_docs/cs/computer architecture/final_project/final_project/testbench_pipelinedProcessor_behav.wcfg -view C:/Users/Dell/Documents/uni_docs/cs/computer architecture/final_project/final_project/waow.wcfg -log simulate.log"
call xsim  tbHazard_behav -key {Behavioral:sim_1:Functional:tbHazard} -tclbatch tbHazard.tcl -view C:/Users/Dell/Documents/uni_docs/cs/computer architecture/final_project/final_project/testbench_RISCV_behav.wcfg -view C:/Users/Dell/Documents/uni_docs/cs/computer architecture/final_project/final_project/testbench_pipelinedProcessor_behav.wcfg -view C:/Users/Dell/Documents/uni_docs/cs/computer architecture/final_project/final_project/waow.wcfg -log simulate.log
if "%errorlevel%"=="0" goto SUCCESS
if "%errorlevel%"=="1" goto END
:END
exit 1
:SUCCESS
exit 0
