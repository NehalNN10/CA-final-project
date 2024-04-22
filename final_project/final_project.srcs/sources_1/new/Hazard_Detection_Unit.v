`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/22/2024 02:08:22 PM
// Design Name: 
// Module Name: Hazard_Detection_Unit
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module Hazard_Detection(
    input [4:0] RS1, RS2, Rd_ID_EX,
    input MemRead_ID_EX,
    output reg stall 
    );

always @(*) 
    begin
        if (MemRead_ID_EX && (Rd_ID_EX == RS1 || Rd_ID_EX == RS2)) 
        begin
            stall = 1;  
        end
        else 
        begin
            stall = 0; 
        end
    end
endmodule
