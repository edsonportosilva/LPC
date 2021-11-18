
% Experimento 5 - LPC
% Codigo auxiliar para ser utilizado na preparacao do experimento.
%
%
% Autor: Edson Porto da Silva
%
% Descricao: este codigo tem a finalidade de servir como guia para
% modelagem da dispersao cromatica em um canal optico (fibra optica).
% Baseado neste codigo o aluno devera responder as questoes da preparacao
% bem como obter os coeficientes dos filtros FIR que sereo utilizados no
% experimento computational no LPC.
%
% Obs.: Este codigo e compativel com o MATLAB e OCTAVE.

clear
clc

% Paremetros da simulacao:
fa  = 128e3;    % frequencia de amostragem (samp_rate)
sps = 16;       % numero de amostras por simbolo
fs  = fa/16;    % frequencia de sinalizacao (frequencia de simbolos)
Ts  = 1/fs;     % perioodo de sinalizacao (periodo de simbolos)
Ntaps = 256;    % numero de coeficientes dos filtros FIR projetados

% Parametros da fibra:
D      = 17e-6;                      % coeficiente de dispersao cromatica da fibra (s/m^2)
lambda = 1550e-9;                    % comprimento de onda da portadora(m)
c      = 3e5;                        % velocidade da luz no vacuo (km/s)
L      = 3000;                       % distancia de propagacao do sinal (km)
beta2  = D*lambda^2/(2*pi*c);        % parametro de dispersao cromatica de segunda ordem da fibra

omega  = 2*pi*linspace(-1/2,1/2, Ntaps)*(fa/16)*1e6; % vetor de frequencias do sinal (escalonado para GHz para efeito didatico)

% Resposta em frequencia da dispersao cromatica:         
Hcd     = exp(1i*(beta2/2)*L*omega.^2);
% Resposta ao impulso (truncada) da dispersao cromatica:
hcd_fir = ifftshift(ifft(Hcd));

% Resposta em frequencia do equalizador zero-forcing:
Hcd_zf     = 1./Hcd;
% Resposta ao impulso (truncada) do equalizador zero-forcing:
hcd_zf_fir = ifftshift(ifft(Hcd_zf));

close all
subplot(1,2,1),plot(abs(hcd_fir),'-*')
hold on,       plot(abs(hcd_zf_fir),'-o')
xlim([1 Ntaps])
title('Valor absoluto da resposta ao impulso')
legend('Canal','Equalizador ZF')
grid on;
subplot(1,2,2),plot(unwrap(angle(hcd_fir)),'-*')
hold on,       plot(unwrap(angle(hcd_zf_fir)),'-o')
xlim([1 Ntaps])
title('Fase da resposta ao impulso')
legend('Canal','Equalizador ZF')
grid on;

% Salva um arquivo .txt com os coefficientes dos filtros FIR no formato 
% requerido pelo GRC:

% Obs: os coeficientes gerados abaixo podem ser exportados para um filtro
% FIR no GRC apenas utilizando ctrl+c, ctrl+v.

filename = ['Exp5_L=' num2str(L) 'km.txt'];
fileID = fopen(filename,'w');

fprintf(fileID,'\n\nCoeficientes do filtro de dispersao cromatica para %d km:\n\n', L);
fprintf(fileID,'[');
for ii = 1:length(omega) 
    if ii ~= length(omega)
        if imag(hcd_fir(ii)) >= 0
            fprintf(fileID, '%.6f+%.6fj, ',real(hcd_fir(ii)), abs(imag(hcd_fir(ii))));
        else
            fprintf(fileID, '%.6f-%.6fj, ',real(hcd_fir(ii)), abs(imag(hcd_fir(ii))));
        end
    else
        if imag(hcd_fir(ii)) >= 0
            fprintf(fileID, '%.6f+%.6fj]',real(hcd_fir(ii)), abs(imag(hcd_fir(ii))));
        else
            fprintf(fileID, '%.6f-%.6fj]',real(hcd_fir(ii)), abs(imag(hcd_fir(ii))));
        end
    end
end

fprintf(fileID, '\n\n');
fprintf(fileID, '\n\nCoeficientes do filtro de equalizador zero-forcing para %d km:\n\n', L);
fprintf(fileID, '[');
for ii = 1:length(omega) 
    if ii ~= length(omega)
        if imag(hcd_zf_fir(ii)) >= 0
            fprintf(fileID, '%.6f+%.6fj, ',real(hcd_zf_fir(ii)), abs(imag(hcd_zf_fir(ii))));
        else
            fprintf(fileID, '%.6f-%.6fj, ',real(hcd_zf_fir(ii)), abs(imag(hcd_zf_fir(ii))));
        end
    else
        if imag(hcd_zf_fir(ii)) >= 0
            fprintf(fileID, '%.6f+%.6fj]',real(hcd_zf_fir(ii)), abs(imag(hcd_zf_fir(ii))));
        else
            fprintf(fileID, '%.6f-%.6fj]',real(hcd_zf_fir(ii)), abs(imag(hcd_zf_fir(ii))));
        end
    end
end
fprintf(fileID, '\n');
fclose(fileID);