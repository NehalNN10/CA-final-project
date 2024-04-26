`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/20/2024 03:36:16 PM
// Design Name: 
// Module Name: IF_ID
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


module IF_ID(
    input clk, reset, stall,
    input [63:0] PC_Out,
    input [31:0] Instruction,
    output reg [63:0] PC_Out_IF_ID,
    output reg [31:0] Instruction_IF_ID
    );
    
    always @(posedge clk or posedge reset) 
    begin
        if (reset == 1 || stall == 1)     //reset values to 0 if reset initiated
            begin
                Instruction_IF_ID <= 0; 
                PC_Out_IF_ID <= 0;
            end
        else                //forward values to register otherwise
            begin
                Instruction_IF_ID <= Instruction; 
                PC_Out_IF_ID <= PC_Out;
            end
    end
endmodule