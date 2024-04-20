`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/20/2024 05:14:21 PM
// Design Name: 
// Module Name: Mux_3x1_64Bit
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


module Mux_3x1(
    input [63:0] A, B, C,
    input [1:0] sel,
    output [63:0] O
    );
    assign O = (sel[1] == 1) ? C : ((sel[0] == 1) ? B : A);
endmodule
