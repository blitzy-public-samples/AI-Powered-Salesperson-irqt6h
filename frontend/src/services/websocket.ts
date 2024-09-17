import { io, Socket } from 'socket.io-client';
import { AppDispatch, addMessage } from 'app/store';

// HUMAN ASSISTANCE NEEDED
// The confidence level for this class is below 0.8. Please review and refine the implementation.
class WebSocketService {
  private socket: Socket;

  constructor(url: string, dispatch: AppDispatch) {
    this.socket = io(url);

    this.socket.on('connect', () => {
      console.log('WebSocket connected');
    });

    this.socket.on('message', (message: any) => {
      dispatch(addMessage(message));
    });

    this.socket.on('error', (error: Error) => {
      console.error('WebSocket error:', error);
    });

    this.socket.on('disconnect', (reason: string) => {
      console.log('WebSocket disconnected:', reason);
    });
  }

  sendMessage(sessionId: string, content: string): void {
    this.socket.emit('send_message', { sessionId, content });
  }
}

export default WebSocketService;